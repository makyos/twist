#!/usr/bin/env python

import os
import sys
import time

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Go to http://dev.twitter.com and create an app. 
# The consumer key and secret will be generated for you after
consumer_key=sys.argv[1]
consumer_secret=sys.argv[2]

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token=sys.argv[3]
access_token_secret=sys.argv[4]

class StdOutListener(StreamListener):
	""" A listener handles tweets are the received from the stream. 
	This is a basic listener that just prints received tweets to stdout.

	"""
	# def on_data(self, data):
	# 	print data
	# 	return True

	# def on_error(self, status):
	# 	print status

	def on_status(self, status):
		# u = status.user.screen_name.encode("utf-8")
		t = status.text.replace("\n"," ").encode("utf-8")
		spc = " ... "
		# print "    %s%s%s " % ("\033[7m", "tw", "\033[0m"),
		sys.stdout.write("")
		for c in t:
			print c,
			sys.stdout.write("")
			time.sleep(0.003)
		print spc,
		sys.stdout.write("")

if __name__ == '__main__':
	sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

	l = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	stream = Stream(auth, l)	
	stream.filter(track=[sys.argv[5]])
