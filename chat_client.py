#!/usr/bin/env python

import chat_gui as gui
import chat_comunication_client as com
import thread

uname = ""
outMessage = ""
ip = "127.0.0.1"

def incomingMessage(m):
	gui.insertChatMessage("",m)
def outcomingMessage():
	gui.insertChatMessage(uname, gui.outMessage.get())
	com.sendMessage(gui.ip.get(),int(gui.port.get()),gui.outMessage.get())
	
try:
	port = int(raw_input("specify a port for listening"))
	thread.start_new_thread(com.receiveMessage,(port,incomingMessage, ))
except:
	print"cant listen to conversation"	
	
gui.init("polly", outcomingMessage)


