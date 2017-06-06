from __future__ import absolute_import

import threading
import select
import json

from websocket import WebSocket as BaseWebSocket


class Replies(object):
    def __init__(self):
        self.replies = {}

    def __getitem__(self, reply_id):
        reply = self.replies[reply_id]
        del self.replies[reply_id]
        return reply

    def __setitem__(self, reply_id, message):
        self.replies[reply_id] = message


class WebSocket(BaseWebSocket):
    def __init__(self, on_event, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)

        self.on_event = on_event

        self.cLock = threading.Condition()
        self.request_id = 1
        self.replies = Replies()

    def connect(self, *args, **kwargs):
        super(self.__class__, self).connect(*args, **kwargs)

        read_thread = threading.Thread(target=self._read_messages)
        read_thread.start()

    def send_message(self, method, params):
        request_id = self.request_id
        self.request_id += 1

        payload = json.dumps({
            'id': request_id,
            'method': method,
            'params': params,
        })
        self.send(payload)

        with self.cLock:
            self.cLock.wait()

        return self.replies[request_id]

    def _read_messages(self):
        while self.connected:
            r, w, e = select.select([self.sock], [], [])

            if r and self.connected:
                with self.cLock:
                    data = self.recv()
                    message = json.loads(data)

                    if 'id' in message:
                        self.replies[message['id']] = message
                        self.cLock.notify()
                    else:
                        self.on_event(message)
