"""
what is a thread
"""

import logging
import time
import requests
import threading
import concurrent.futures


def thread_function(name, domain_name):

    logging.info("Thread %s: starting", name)
    result = requests.get(f"http://{domain_name}", timeout=3).text
    print(f"Domain: {domain_name}, Length:{len(result)}")
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    # logging.info("Main    : before creating thread")
    # domain_name = "tmall.com"
    # # non daemon
    # # x = threading.Thread(target=thread_function, args=(1,domain_name))
    # # daemon version
    # x = threading.Thread(target=thread_function, args=(1,domain_name), daemon=True)

    # logging.info("Main    : before running thread")
    # x.start()
    # logging.info("Main    : wait for the thread to finish")
    # x.join()
    # logging.info("Main    : all done")
    # domain_name = "tmall.com"
    # with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    #     executor.map(thread_function, range(3))

    threads = list()
    domain_names = ["tmall.com", "google.com", "yahoo.com", "youtube.com", "tmall.com","baidu.com", "qq.com", "sohu.com", "facebook.com", "taobao.com"]

    # for x, domain in enumerate(domain_names):
    #     x = threading.Thread(target=thread_function,args=(x,domain))

    # for index in range(3):



    # start = time.time()
    # for x, domain in enumerate(domain_names):
    #     logging.info("Main    : create and start thread %d.", x)
    #     # x = threading.Thread(target=thread_function, args=(index,))
    #     x = threading.Thread(target=thread_function, args=(x, domain))
    #     threads.append(x)
    #     x.start()

    # for index, thread in enumerate(threads):
    #     logging.info("Main    : before joining thread %d.", index)
    #     thread.join()
    #     logging.info("Main    : thread %d done", index)
    # end = time.time()
    # print("=" * 10)
    # print(f"Threaded Total Time:{ end - start}")
    # print("=" * 10)
    
    start = time.time()
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        for x, domain in enumerate(domain_names):
            executor.submit(thread_function,x, domain)

    end = time.time()
    print("=" * 10)
    print(f"Threaded Total Time:{ end - start}")
    print("=" * 10)

    start = time.time()
    for x, domain in enumerate(domain_names):
        thread_function(x, domain)
        end = time.time()
    print("=" * 10)
    print(f"Sequental Total Time:{ end - start}")
    print("=" * 10)
