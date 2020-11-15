# TCP client

import socket
import threading
from datetime import datetime

HOST = '127.0.0.1'
PORT = 5050
CONNECTED = True
CONNECTION_MSG = '!CONNECT:'
DISCONNECTION_MSG = "!DISCONNECT"
CALLBACK_MSG = '!CALLBACK'

username = input("Welcome, enter your name: ")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
sock.send((CONNECTION_MSG+username).encode('utf-8'))

def callback():
	i = 1
	while CONNECTED:
		now = datetime.now().minute
		if i == 1:
			i = 0
			after = now + 2
			if after >= 60:
				after -= 60
		if after == now:
			i = 1
			print("!CALLBACK")
			try: sock.send(CALLBACK_MSG.encode('utf-8'))
			except: break

def receiving_msg():
	while CONNECTED:
		try:
			received_data = sock.recv(1024)
			msg = received_data.decode('utf-8')
			if not msg:
				print("[ERROR] Server stopped")
				break
			else:
				print(msg)
		except:
			print("[ERROR] you disconnected from the server or server stopped")
			break

thread1 = threading.Thread(target=receiving_msg, daemon=True)
thread1.start()

thread2 = threading.Thread(target=callback, daemon=True)
thread2.start()

while CONNECTED:
	try:
		msg = input()
		sock.send(msg.encode('utf-8'))
		if msg == DISCONNECTION_MSG or thread1.is_alive() == False:
			CONNECTED = False
	except:
		try: sock.send(DISCONNECTION_MSG.encode('utf-8'))
		except: pass
		finally: CONNECTED = False

thread1.join()
sock.close()
