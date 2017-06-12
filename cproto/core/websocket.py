from __future__ import absolute_import

import threading
import select
import json
try:
    from queue import Queue
except ImportError:
    from Queue import Queue

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

        self._on_event = on_event

        self.request_id = 1
        self.cLock = threading.Condition()
        self.replies = Replies()
        self.events = Queue()

    def connect(self, *args, **kwargs):
        super(self.__class__, self).connect(*args, **kwargs)

        threading.Thread(target=self._read_messages).start()
        threading.Thread(target=self._process_events).start()

    def close(self):
        # Terminates blocking `get` call on events processing thread
        self.events.put(None)
        return super(self.__class__, self).close()

    def send_message(self, method, params):
        request_id = self.request_id
        self.request_id += 1

        payload = json.dumps({
            'id': request_id,
            'method': method,
            'params': params,
        })
        self.send(payload)

        # Wait until response is ready
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

                    # If id is present -> notifies main thread to return this message as a reply
                    # Otherwise puts message into events queue so it will be dispatched as event
                    if 'id' in message:
                        self.replies[message['id']] = message
                        self.cLock.notify()
                    else:
                        self.events.put(message)

    def _process_events(self):
        while self.connected:
            event = self.events.get()

            # `None` is standing as a null terminator event
            if event is None:
                break

            self._on_event(event)
