import time
import threading
import concurrent.futures

def FUNCTION(name, arg2):
	print("Thread %s: starting", name)
	print("fruit: " + arg2)
	time.sleep(2) #seconds could be : requests.get(.....)
	print("Thread %s: finishing", name)

fruits = ["apple", "banana", "orange"]
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
	for x, item in enumerate(fruits):
		executor.submit(FUNCTION,x,item)