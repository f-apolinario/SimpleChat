import socket
ip="127.0.0.1"
def sendMessage(ip,port,message):
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.sendto(message, (ip,port))
	
def receiveMessage(port,callback):
	global ip
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.bind((ip,port))
	while True:
		data,addr= sock.recvfrom(1024)
		callback(data)
	