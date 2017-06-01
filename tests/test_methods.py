from cproto import CProto


class TestMethods:

    def setup(self):
        self.cp = CProto()

    def teardown(self):
        self.cp.close()

    def test_navigate_reply(self):
        res = self.cp.Page.navigate(url='https://google.com/')

        assert res['id'] == 1

        res = self.cp.Page.navigate(url='https://github.com/')

        assert res['id'] == 2
