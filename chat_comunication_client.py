import socket

def sendMessage(ip,port,message):
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.sendto(message, (ip,port))
	
def receiveMessage(ip,port,callback):
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.bind((ip,port))
	while True:
		data,addr= sock.recvfrom(1024)
		callback(data)
	