from cproto import CProto


def test_websocket_connection():
    cp = CProto()
    assert cp.ws.connected is True, 'Should be connected to CDP'

    cp.close()
    assert cp.ws.connected is False, 'Should be disconnected from CDP'
