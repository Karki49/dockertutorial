import logging
import os
import time
import random

def do_logging():
	rID = random.randint(1, 1000)
	passedValue = os.environ.get('passedValue', "oops")
	for i in range(10):
		logging.error("randomID:%s passedValue:%s iter:%s" %(rID, passedValue, i))
		time.sleep(5)

if __name__=='__main__':
	do_logging()