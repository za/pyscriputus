#!/usr/bin/python

import urllib
import re

# the html scrap function
def scrap(url): 
	sock = urllib.urlopen(url)
	htmlSource = sock.read()
	sock.close()
	print htmlSource

# the regex function():
#def regex():


# the main function
def main():
	scrap('http://localhost/za')
#	regex()
	
# standard boilerplate to call the main() function.
if __name__ == '__main__':
	main()
