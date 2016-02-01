#!/usr/bin/env python
from Tkinter import *
from ScrolledText import *

GUI = Tk()
GUI.geometry("750x600")
GUI.title("Simple Chat")

uname = ""
outMessage = StringVar()
s_ip = StringVar()
s_port = StringVar()
u_ip = ""
u_port = ""
ChatBox = ScrolledText(GUI)
r = 0
c =0

def insertChatMessage(username,message):
	ChatBox.insert(INSERT,username + ": " + message + "\n")


def gui_init(callback_send):	
	global uname, outMessage, ChatBox,u_ip,u_port,s_ip,s_port,r,c	
	
	#user details
	SenderLabel = Label(GUI,text= "User Details")
	SenderLabel.grid(row=r,column=0)
	r+=1	
	IPLabel = Label(GUI,text= "IP:")
	IPLabel.grid(row=++r,column=c)
	IPBox = Label(GUI,text= u_ip) 
	c+=1
	IPBox.grid(row=r,column=++c)
	r+=1	
	c=0
	IPLabel = Label(GUI,text= "Port:")
	IPLabel.grid(row=r,column=c)
	c+=1	
	IPBox = Label(GUI,text= u_port) 
	IPBox.grid(row=r,column=c)
	
	#IP and Port specification gui
	c = 0
	SenderLabel = Label(GUI,text= "Sender address")
	r+=1
	SenderLabel.grid(row=r,column=0)
	IPLabel = Label(GUI,text= "IP:")
	r+=1	
	IPLabel.grid(row=r,column=c)
	IPBox = Entry(GUI, textvariable = s_ip) 
	c+=1
	IPBox.grid(row=r,column=c)
	c = 0
	r+=1
	PortLabel = Label(GUI,text= "Port:")
	PortLabel.grid(row=r,column=c)
	PortBox = Entry(GUI, textvariable = s_port) 
	c+=1
	PortBox.grid(row=r,column=c)
	c = 0
	
	#Message content
	r+=1
	MessageLabel = Label(GUI,text= "Message")
	MessageLabel.grid(row=r,column=c)
	r+=1
	MessageLabel = Label(GUI,text= "Message:")
	MessageLabel.grid(row=r,column=c)
	MessageBox = Entry(textvariable = outMessage)
	c+=1
	MessageBox.grid(row=r,column=c)
	
	r+=1
	SendButton = Button(text = "Send", command = callback_send)
	SendButton.grid(row=r, column=0)
	
	#Chat history messages
	c=0
	r+=1	
	ChatLabel = Label(GUI,text= "Message:")
	ChatLabel.grid(row=r,column=c)
	r+=1
	ChatBox.grid(row=r,column=c)
	
	mainloop()

def init(username, ip, port, send_callBack):
	global uname, u_ip, u_port
	uname = username
	u_ip = ip
	u_port = port
	print "%s" % uname
	gui_init(send_callBack)
	

#init("polly", SEND_CMD)

