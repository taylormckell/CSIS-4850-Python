# Taylor Cella
# CLI Sockets Assignment

import socket, sys, optparse

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Creates an option parser
parser = optparse.OptionParser()

# Adds an option for the server address
parser.add_option("-s", "--server_address", dest="srv_address", 
help = "Enter a SERVER address", metavar = "SERVER")

# Adds an option for the port number
parser.add_option("-p", "--port_number", dest="p_num", 
help = "Enter a PORT address", metavar = "PORT")

# Adds an option for the message
parser.add_option("-m", "--message", dest="message", 
help = "Please write a MESSAGE", metavar = "MESSAGE")

# Adds options to the parser
(options, args) = parser.parse_args()

srv_addr = options.srv_address

port_num = options.p_num

server_addr = (srv_addr, int(port_num))

sock.connect(server_addr)

try:
	msg = options.message
	msg = msg.encode("utf-8")
	sock.sendall(msg)
	data = sock.recv(1024)
	print("Received message: %s " % data.decode("utf-8"))
finally:
	sock.close()
