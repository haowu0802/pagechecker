"""Test for pagechecker
"""
import unittest
import pagechecker


# tests
class TestPageChecker(unittest.TestCase):
    def test_can_get_page(self):
        url = 'http://google.com'
        worker = pagechecker.PageCheckerWorker(url, 5)
        pagecheck_log = worker.check_page()
        print pagecheck_log
        self.assertIn(url, pagecheck_log)
        self.assertIn("Bytes", pagecheck_log)

    def test_can_detect_timeout(self):
        url = 'http://httpbin.org/delay/10'
        worker = pagechecker.PageCheckerWorker(url, 5)
        pagecheck_log = worker.check_page()
        print pagecheck_log
        self.assertIn(url, pagecheck_log)
        self.assertIn("TIMEOUT", pagecheck_log)

    #TODO: a test checking the thread pool for number of threads and status

if __name__ == "__main__":
    unittest.main()
