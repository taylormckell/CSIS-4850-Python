# Taylor Cella
# CLI Sockets Assignment

import socket, sys, optparse

# Creates a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Creates an option parser
parser = optparse.OptionParser()

# Adds an option for the server address
parser.add_option("-s", "--server_address", dest="srv_address", 
help = "Enter a SERVER address", metavar = "SERVER")

# Adds an option for the port number
parser.add_option("-p", "--port_number", dest="p_num", 
help = "Enter a PORT address", metavar = "PORT")

# Adds options to the parser
(options, args) = parser.parse_args()

srv_addr = options.srv_address

port_num = options.p_num

# Creates a tuple to bind to the socket
server_addr = (srv_addr, int(port_num))

sock.bind(server_addr)

sock.listen(1)

print("Listening at address: %s " % (srv_addr))

print("Listening at address: %d " % (int(port_num)))

while True:
	connection, client_addr = sock.accept()
	print("Connection received from %s on port %d" % client_addr)
	try:
		while True:
			data = connection.recv(1024)
			print("Received message: %s" % data.decode("utf-8"))
		if data:
			connection.sendall(data)
		else:
			break
	finally:
		connection.close()
