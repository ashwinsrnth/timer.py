import time
import numpy as np
from numpy.testing import *
import timer

class TestLogging:

    def setup(self):
        self.log = timer.Log()

    def test_single_event(self):
        for sleep_times in [1e-5, 1e-4, 1e-3, 1e-2, 1e-1]:
            self.log.create_event('event_1')
            self.log.start('event_1')
            time.sleep(0.1)
            self.log.stop('event_1')
            assert_allclose(self.log.logDict['event_1'].stop_time - self.log.logDict['event_1'].start_time, 0.1, rtol=0.01)

    def test_start_without_create(self):
        assert_raises(UnboundLocalError, self.log.start, 'event_nonexistent')

    def test_stop_without_create(self):
        assert_raises(UnboundLocalError, self.log.stop, 'event_nonexistent')

    def test_stop_without_start(self):
        self.log.create_event('event_1')
        assert_raises(ValueError, self.log.stop, 'event_1')