#!/usr/bin/python

import urllib
import re

# the html scrap function

def extractURL(url):
	sock = urllib.urlopen(url)
	source = sock.read()
	sock.close()
	
	url = re.findall(r'<a href=http://.+</a>', source)
	print url

def scrap(url): 
	sock = urllib.urlopen(url)
	htmlSource = sock.read()
	sock.close()
	return htmlSource

# the find function():
def find(pat, text):
	match = re.search(pat,text)
	if match: 
		print match.group()
	else:
		print 'not found'

# the main function
def main():
#	scrap('http://localhost/za')
#	print htmlSource
#	find('http', htmlSource)	
	extractURL('http://localhost/za')	

# standard boilerplate to call the main() function.
if __name__ == '__main__':
	main()
