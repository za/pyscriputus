#!/usr/bin/python

import urllib
import re

# the html scrap function

def extractURL(url):
	sock = urllib.urlopen(url)
	source = sock.read()
	sock.close()

	# how to store in a variable? tuple? dictionary? 	
	url = re.findall(r'http://\w+.\w+', source)
	
	dict = {'URL':'code'}	
	for u in url: 
		status = urllib.urlopen(u)
		code = status.getcode()
		print u, code	

#def scrap(url): 
#	sock = urllib.urlopen(url)
#	htmlSource = sock.read()
#	sock.close()
#	return htmlSource

# the main function
def main():
	extractURL('http://localhost/za')	

# standard boilerplate to call the main() function.
if __name__ == '__main__':
	main()
