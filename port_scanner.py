import optparse

from socket import * 
from threading import *

def connScan(tgtHost, tgtPort):
	""" creates a socket which connects to the host and port, 
		then opens the socket and sends a message to the host """
	try:
		connSkt = socket(AF_INET, SOCK_STREAM)
		connSkt.connect((tgtHost, tgtPort))

		print '[+]%d/tcp open'% tgtPort
		print '[+]' + 'Connection successful\n'
	
	# if it encounters an error, it will print the error and show that 
	# the port is closed 
	except Exception as e:
		print(e)
		print '[-]%d/tcp closed'% tgtPort	
	
	# ends the program and closes the connection
	finally:
		connSkt.close()
	 
def portScan(tgtHost, tgtPorts):
	""" gets the host name and address, and prints them to the terminal"""
	try:
		tgtIP = gethostbyname(tgtHost)
	
	# If it cannot find the host name, it'll give an error message"
	except:
		 print "[-] Cannot resolve '%s': Unknown host" %tgtHost
		 return
	
	# Gets the address name
	try:
		 tgtName = gethostbyaddr(tgtIP)
		 print '\n[+] Scan Results for: ' + tgtName[0]
	except:
		print '\n[+] Scan Results for: ' + tgtIP
	
	setdefaulttimeout(1)
	
	for tgtPort in tgtPorts:
		t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
		t.start()

def main():
	""" Creates parser and defines parser options """
	
	parser = optparse.OptionParser('port_scanner.py '+\
	 '-H <target host> -p <target port>. If you dont give a hostname' +
	' or a port, a connection will be established with a pre-defined' +
	 ' host and port list.')
	
	parser.add_option('-H', dest='tgtHost', type='string', \
	 help='specify target host')
	
	parser.add_option('-p', dest='tgtPort', type='string', \
	 help='specify target port[s] separated by comma, and surround \
	 multiples by quotation marks.')
	
	# ties the parser arguments to the parser
	(options, args) = parser.parse_args()
	
	tgtHost = options.tgtHost
	tgtPorts = str(options.tgtPort).split(', ')
	
	# if no parameters are given, the usage will be printed as well as
	# a default host and port list
	if (tgtHost == None) | (tgtPorts[0] == None):
		print parser.usage
		# Creates a default to show the options as nmap would for the 
		# Windows 7 machine
		tgtHost = '10.0.2.4'
		tgtPorts= [135,139,445,5357,49152,49153,49154,49155,49156,49157]
		portScan(tgtHost, tgtPorts)
		exit(0)
	portScan(tgtHost, tgtPorts)	

if __name__ == "__main__":
		main()
