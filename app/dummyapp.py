import logging
import os
import time

def do_logging():
	someID = os.environ.get('randomName', "oops")
	for i in range(10):
		logging.error("hello from %s . iter: %s" %(someID, i))
		time.sleep(5)

if __name__=='__main__':
	do_logging()