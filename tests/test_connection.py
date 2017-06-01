from cproto import CProto


def test_websocket_connection():
    cp = CProto()
    assert cp.ws.connected is True

    cp.close()
    assert cp.ws.connected is False
