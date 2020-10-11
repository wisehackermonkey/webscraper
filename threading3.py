import concurrent.futures
import logging
import queue
import random
import threading
import time
import requests
import json
import csv 
results = []
FILE_NAME = f"./scraping_results_{time.time()}" + ".json"
CSV_FILE = "./top-1m-internet-domains.csv"
END = 1000

def save_file(file_name, data):
    with open(file_name, "w", encoding="utf8") as scraped_domains_file:
        serialize_results = json.dumps(data)
        scraped_domains_file.write(serialize_results)

def read_csv(file_name):
        with open(file_name, "r") as website_csv:
            csvreader = csv.reader(website_csv, delimiter=",")
            websites_list_accumulator = []
            for x, domain in enumerate(csvreader):
                if x < END:
                    # "12313, google.com" <- grab the domain name only = domain[1]
                    websites_list_accumulator.append(domain[1])
            return websites_list_accumulator
def producer(queue, event, domain_name):
    """Pretend we're getting a number from the network."""
    while not event.is_set():
        start = time.time()
        print(".",end="")
        text_result = requests.get(f"http://{domain_name}", timeout=3).text
        end = time.time()
        logging.info(f"Producer got {domain_name}: {len(text_result)}", )
        results.append(
            {
                "domain": domain_name,
                "epoch": time.time(),
                "loadtime": f"{end - start} seconds",
                "result": text_result
            })

        queue.put(text_result)

    logging.info("Producer received event. Exiting")
    event = threading.Event()


# domain_names = ["tmall.com", "google.com", "yahoo.com", "youtube.com", "baidu.com", "qq.com", "sohu.com", "facebook.com", "taobao.com", "apple.com"]

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    # logging.basicConfig(format=format, level=logging.ERROR, datefmt="%H:%M:%S")

    pipeline = queue.Queue(maxsize=1000)
    event = threading.Event()

    domain_names = read_csv(CSV_FILE)
    print("\n\n\n")
    start = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=END) as executor:
        for domain in domain_names:
            executor.submit(producer, pipeline, event, domain)

        time.sleep(0.1)
        logging.info("Main: about to set event")
        event.set()
    end = time.time()
    print("\n\n\n")
    logging.info(f"Total Results: {len(results)}")

    print(f"Total Time: {end - start}")
    print(f"Total Results: {len(results)}")

    save_file(FILE_NAME, results)
