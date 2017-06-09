from cproto import CProto


def capture_screen(_):
    payload = cp.Page.captureScreenshot()
    data = payload['result']['data'].decode('base64')

    with open('output.jpeg', 'wb') as f:
        f.write(data)

    cp.close()


if __name__ == '__main__':
    cp = CProto()
    cp.Page.enable()
    cp.Page.loadEventFired = capture_screen
    cp.Page.navigate(url='https://github.com')
