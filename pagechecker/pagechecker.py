"""Project Assignment B
"""
from time import time, sleep
from datetime import datetime
import urllib2
from threading import Thread

# TODO: take a external file as url list input
url_list = [
    ('http://cnn.com',10),
    ('http://google.ca',20),
    ('http://cnn.com',15),
    ('http://httpbin.org/delay/20',5)
]

class PageCheckerWorker(object):
    
    def __init__(self, url, interval):
        self.url = url
        self.interval = interval

    def check_page(self):
        timestamp = time()
        self.time_check_point = timestamp
        # timeout should never be longer than interval
        # if the page is expected to load longer than interval, then interval needs to be extended longer
        try:
            page_result = urllib2.urlopen(self.url, timeout=1)
            content_length = len(page_result.read())
            # TODO: refactor datetime formats into a helper function
            return "%s - %s - %s Bytes" % (datetime.fromtimestamp(timestamp).strftime('%d/%m/%y %H:%M:%S'), self.url, content_length)
        except IOError as err:
            return "%s - %s - TIMEOUT" % (datetime.fromtimestamp(timestamp).strftime('%d/%m/%y %H:%M:%S'), self.url)

# py2 uses functions as thread runner, py3 uses object
def worker_runner(worker):
    while True:
        print worker.check_page()
        time_till_next_check = time() - worker.time_check_point
        sleep_time = worker.interval - time_till_next_check
        #print 'times:', worker.time_check_point, time_till_next_check, sleep_time
        if sleep_time > 0:
            sleep(sleep_time)

# main
def run():
    # initiate worker threads
    for url, interval in url_list:
        worker = PageCheckerWorker(url,interval)
        t = Thread(target=worker_runner, args=(worker,))
        t.daemon = True # thread dies with process
        t.start()

    # TODO: make termination of process more user friendly, instead of using ctrl-c
    while True:
        pass

if __name__ == '__main__':
    run()