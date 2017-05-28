from __future__ import absolute_import

import json
import base64
import threading
import select
from os import path
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

from websocket import create_connection, WebSocket

from cproto.domains.factory import DomainFactory


ROOT_DIR = path.abspath(path.dirname(path.dirname(__file__)))


class WS(WebSocket):
    def __init__(self, on_message):
        super(self.__class__, self).__init__()

        self.on_message = on_message

    def connect(self, *args, **kwargs):
        super(self.__class__, self).connect(*args, **kwargs)

        read_th = threading.Thread(target=self.read_stream)
        read_th.start()

    def read_stream(self):
        while self.connected:
            data = self.recv()
            if data:
                self.on_message(json.loads(data))

class CProto(object):

    def __init__(self, host='127.0.0.1', port=9222):
        res = urlopen('http://{0}:{1}/json'.format(host, port))

        url = json.loads(res.read())[0]['webSocketDebuggerUrl']
        self.ws = WS(on_message=self.on_message)
        self.ws.connect(url)

        with open(path.join(ROOT_DIR, 'resources/protocol.json'), 'rb') as f:
            data = json.loads(f.read())

        for d in data['domains']:
            domain_name = d['domain']

            # Build Domain Class from protocol
            DomainClass = DomainFactory(domain_name, d['commands'])

            # Set WebSocket attribute
            setattr(DomainClass, 'ws', self.ws)

            # Set Domain's Class as a property
            setattr(self, domain_name, DomainClass)

    def on_message(self, message):
        if 'method' in message:
            domain_name, method_name = message['method'].split('.')
            domain = getattr(self, domain_name)

            if hasattr(domain, method_name):
                getattr(domain, method_name)(message['params'])

    def close(self):
        self.ws.close()
