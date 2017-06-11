from time import sleep

from cproto import CProto


class TestEvents:

    def setup(self):
        self.cp = CProto()
        self.Page = self.cp.Page
        self.Page.enable()

    def teardown(self):
        self.cp.close()

    def test_events(self):
        def callback(_): self.events_fired += 1

        self.events_fired = 0
        self.Page.frameStartedLoading = callback
        self.Page.frameNavigated = callback
        self.Page.domContentEventFired = callback
        self.Page.loadEventFired = callback
        self.Page.frameStoppedLoading = callback

        self.Page.navigate(url='about:blank')

        sleep(0.3)

        assert self.events_fired == 5, 'Should receive all events'
