#!/usr/bin/env python
from Tkinter import *
from ScrolledText import *

GUI = Tk()
GUI.geometry("750x600")
GUI.title("Simple Chat")

uname = ""
outMessage = StringVar()
ip = StringVar()
port = StringVar()
ChatBox = ScrolledText(GUI)

def insertChatMessage(username,message):
	ChatBox.insert(INSERT,username + ": " + message + "\n")


def gui_init(callback_send):	
	global uname, outMessage, ChatBox,ip,port	
	#IP and Port specification gui
	IPLabel = Label(GUI,text= "IP:")
	IPLabel.grid(row=0,column=0)
	IPBox = Entry(GUI, textvariable = ip) 
	IPBox.grid(row=0,column=1)
	PortLabel = Label(GUI,text= "Port:")
	PortLabel.grid(row=1,column=0)
	PortBox = Entry(GUI, textvariable = port) 
	PortBox.grid(row=1,column=1)
	
	#Message content
	MessageLabel = Label(GUI,text= "Message:")
	MessageLabel.grid(row=2,column=0)
	MessageBox = Entry(textvariable = outMessage)
	MessageBox.grid(row=2,column=1)
	SendButton = Button(text = "Send", command = callback_send)
	SendButton.grid(row=3, column=0)
	
	#Chat history messages
	ChatLabel = Label(GUI,text= "Message:")
	ChatLabel.grid(row=4,column=0)
	ChatBox.grid(row=4,column=1)
	mainloop()

def init(username, send_callBack):
	global uname
	uname = username
	print "%s" % uname
	gui_init(send_callBack)
	

#init("polly", SEND_CMD)

