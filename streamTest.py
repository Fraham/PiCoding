import time
from ISStreamer.Streamer import Streamer

key = raw_input('Enter the key')

logger = Streamer(bucket="Stream Example", client_key=key)

logger.log("My Messages", "Stream Starting")
for num in range(1, 20):
	time.sleep(0.1)
	logger.log("My Numbers", num)
	if num%2 == 0:
		logger.log("My Booleans", "false")
	else:
		logger.log("My Booleans", "true")
	if num%3 == 0:
		logger.log("My Events", "pop")
	if num%10 == 0:
		logger.log("My Messages", "Stream Half Done")
logger.log("My Messages", "Stream Done")
