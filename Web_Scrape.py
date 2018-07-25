from anon_browser import *
from BeautifulSoup import BeautifulSoup
import os
import optparse
import re

def printLinks(url):
	"""Opens an anonymous browser, reads the url given, and reads the 
	page associated with the URL. From this page, links are listed."""
	ab = anonBrowser()
	ab.anonymize()
	page = ab.open(url)
	html = page.read()
	try:
		# Uses a regular expression to find all with the html tag 'href'
		# Finds all with any single character, and allows for * to be
		# Within the link 
		# regex also gives more information about sources from the site
		# itself, like where it is hosted and where some of the elements
		# such as font or themes came from as well.
		print '[+] Printing Links From Regex.'
		link_finder = re.compile('href="(.*?)"')
		# Finds these regular expressions within the page
		links = link_finder.findall(html)
		# Prints the links
		for link in links:
			print link
	except:
		pass
	try:
		# Prints links from the package imported, only shows links 
		# within the page rather than more information like regex does
		print '\n[+] Printing Links From BeautifulSoup.'
		soup = BeautifulSoup(html)
		# Finds all tags that start with 'a' in HTML
		links = soup.findAll(name='a')
		for link in links:
			# if link also has href, it's legitimate and will be printed
			if link.has_key('href'):
				print link['href']
	except:
		pass

def main():
	""" Creates parser options for usage, runs the program """
	parser = optparse.OptionParser('usage%prog ' +\
	'-u <target url>')
	parser.add_option('-u', dest='tgtURL', type='string',\
	help='specify target url')
	(options, args) = parser.parse_args()
	url = options.tgtURL
	# if no url is given, print out the usage 
	if url == None:
		print parser.usage
		exit(0)
	else:
		printLinks(url)
		
if __name__ == '__main__':
	main()
