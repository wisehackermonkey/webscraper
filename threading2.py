# by oran collins
# github.com/wisehackermonkey
# oranbusiness@gmail.com
# 20201010

import time
import threading
import concurrent.futures
import queue
import requests

class Scrape():
    """
    locking thread example
    """
    def __init__(self):
        self.results = []
        self._lock = threading.Lock()


    def update_results_non_lock(self, domain_name):
            results = self.results
            print(f"Thread started: {domain_name}")
            response = requests.get(f"http://{domain_name}", timeout=3).text
            print(f"Thread started: {domain_name}, End Length {len(response)}")
            results.append(response)
            self.results = results


    def update_results(self, domain_name):
        with self._lock:
            results = self.results
            print(f"Thread started: {domain_name}")
            response = requests.get(f"http://{domain_name}", timeout=3).text
            print(f"Thread started: {domain_name}, End Length {len(response)}")
            results.append(response)
            self.results = results
        
    
# def scrape_url()
domain_names = ["tmall.com", "google.com", "yahoo.com", "youtube.com", "tmall.com","baidu.com", "qq.com", "sohu.com", "facebook.com", "taobao.com"]



if __name__ == "__main__":
    print("started")
    # scraper = Scrape()
    # with concurrent.futures.ThreadPoolExecutor(max_workers=10) as runner:
    #     for domain in domain_names:
    #         print(f"Sumbitting Thread for domain: {domain}")
    #         runner.submit(scraper.update_results,domain)
    # print(len(scraper.results))

    scraper2 = Scrape()

    for domain in domain_names:
        print(f"Sumbitting Thread for domain: {domain}")
        scraper2.update_results_non_lock(domain)
    print(len(scraper2.results))