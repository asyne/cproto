from __future__ import absolute_import

import json
from os import path
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

from cproto.core.websocket import WebSocket
from cproto.domains.factory import DomainFactory

ROOT_DIR = path.abspath(path.dirname(path.dirname(__file__)))


class CProto(object):

    def __init__(self, host='127.0.0.1', port=9222):
        res = urlopen('http://{0}:{1}/json'.format(host, port))

        url = json.loads(res.read())[0]['webSocketDebuggerUrl']
        self.ws = WebSocket(on_event=self._on_event)
        self.ws.connect(url)

        with open(path.join(ROOT_DIR, 'resources/protocol.json'), 'rb') as f:
            data = json.loads(f.read())

        for d in data['domains']:
            domain_name = d['domain']

            # Build Domain Class from protocol
            DomainClass = DomainFactory(domain_name, d['commands'])

            # Set WebSocket attribute
            DomainClass.ws = self.ws

            # Set Domain's Class as a property
            setattr(self, domain_name, DomainClass())

    def close(self):
        self.ws.close()

    def _on_event(self, message):
        domain_name, method_name = message['method'].split('.')
        domain = getattr(self, domain_name)

        if hasattr(domain, method_name):
            getattr(domain, method_name)(message['params'])
