#!/usr/bin/env python

import chat_gui as gui
import chat_comunication_client as com
import thread
import json

with open('config.json') as d:
	config = json.load(d)
uname = config["nick"]
outMessage = ""
u_ip = config["ip"]
u_port = int(config["port"])

def incomingMessage(m):
	gui.insertChatMessage("friend",m)
def outcomingMessage():
	gui.insertChatMessage(uname, gui.outMessage.get())
	com.sendMessage(gui.s_ip.get(),int(gui.s_port.get()),gui.outMessage.get())
	
try:
	thread.start_new_thread(com.receiveMessage,(u_ip,u_port,incomingMessage, ))
except:
	print"cant listen to conversation"	
	
gui.init("me", u_ip, u_port,outcomingMessage)


