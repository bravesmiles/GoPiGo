#!/usr/bin/env python 

# This is a basic example for a socket server for the GoPiGo.
# This allows the client to connects can be used to respond to the commands and run the GoPiGo
# the socket server is running on Port 5005 on localhost

# Send a single byte command to the server from the client:
#	s 	- stop
#	f 	- move forward
#	b 	- move back
#	l	- turn left
#	r	- turn right

import socket
import gopigo
import sys
import time

# Listen on localhost at port 5005
#TCP_IP = '127.0.0.1' 
TCP_IP = '172.20.10.6'
TCP_PORT = 5005
BUFFER_SIZE = 20

# Create a TCP socket and bind the server to the port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
print "Server Started"

while True:
	#Wait for incomming connections
	s.listen(1)
	
	#Accept an incoming connection
	conn, addr = s.accept()
	
	print '\nConnection address:', addr
	while 1:
		#Check the data
		data = conn.recv(BUFFER_SIZE)
		if not data: break	
		print "received data:", data
		if len(data) <> 1:
			print ("Invalid command")
			conn.send("Invalid command")
		elif data=='w':
			gopigo.fwd()
			conn.send("Moving forward")
		elif data=='x':
			gopigo.stop()
			conn.send("Stopping")
		elif data=='s':
			gopigo.bwd()
			conn.send("Moving back")
		elif data=='a':
			gopigo.left()
			conn.send("Turning left")
		elif data=='d':
			gopigo.right()
			conn.send("Turning right")
		elif data=='t':
                        gopigo.increase_speed()
                        conn.send("Increase speed")
                elif data=='g':
                        gopigo.decrease_speed()
                        conn.send("Decrease speed")
                elif data=='v':
                        # print gopigo.volt(), 'V'
                        conn.send(str(gopigo.volt()))
                elif data=='l':
                        gopigo.led_on(0)
			gopigo.led_on(1)
			time.sleep(1)
			gopigo.led_off(0)
			gopigo.led_off(1)
                        conn.send("Flash LED")		
		else:
			print ("Invalid command")
			conn.send("Invalid command")
	conn.close()
