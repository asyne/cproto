from cproto import CProto


class TestMethods:

    def setup(self):
        self.cp = CProto()

    def teardown(self):
        self.cp.close()

    def test_navigate_reply(self):
        assert self.cp.Page.navigate(url='about:blank')['id'] == 1, 'Should have initial request id'
        assert self.cp.Page.navigate(url='about:blank')['id'] == 2, 'Should have (initial + 1) request id'
