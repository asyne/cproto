import json
import base64

from cproto import CProto


def do_capture():
    cp = CProto()
    payload = json.loads(cp.Page.captureScreenshot())
    data = base64.b64decode(payload['result']['data'])

    with open('output.jpeg', 'wb') as f:
        f.write(data)


if __name__ == '__main__':
    do_capture()
