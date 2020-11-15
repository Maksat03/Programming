# TCP server

import socket
from threading import Thread
from config import *

users = []

print("[log] Сервер запускается...")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen()

print(f"[log] Сервер прослушивает ({str(HOST)}, {str(PORT)})")

def sock_close():
	while True:
		try:
			input()
		except:
			sock.close()
			break

def handle_client(conn, index, username):
	connected = True

	while connected:
		try:
			received_data = conn.recv(1024)
			msg = received_data.decode('utf-8')

		except:
			users[index] = None
			connected = False
			msg = DISCONNECTION_MSG

		finally:
			if not msg.isspace():
				msg = msg.lstrip()
				msg = msg.rstrip()

				if msg == CALLBACK_MSG:
					print("!CALLbACK")

				else: 
					if msg == DISCONNECTION_MSG:
						users[index] = None
						connected = False
						msg = f'[log] {username} отсоединился'
						try: conn.send('[log] До скорого, вы отсоединились'.encode('utf-8'))
						except: pass

					else:
						conn.send(f'[log] {username}: {msg}'.encode('utf-8'))
						msg = f'[log] {username}: {msg}'

					for i, user in enumerate(users):
						if i != index:
							try: user.send(msg.encode('utf-8'))
							except: pass

					print(msg)

	conn.close()

Thread(target=sock_close, daemon=True).start()

while True:
	try:
		conn, addr = sock.accept()
		conn.settimeout(15)
		print(f"[log] Новое подключение с {addr}")
	except:
		break
	else:
		try: 
			print(f"[log] Ждём сообщение от {addr}")
			received_data = conn.recv(1024)
		except: print("[log] Тайм-аут или сервер упал")
		else:
			msg = received_data.decode('utf-8')
			if CONNECTION_MSG in msg:
				print(f"[log] {addr} подключился к чату")
				conn.settimeout(300)
				username = msg.split(":")[1]
				thread = Thread(target=handle_client, args=(conn, len(users), username), daemon=True)
				thread.start()
				conn.send('[log] Добро пожаловать, вы подключились'.encode('utf-8'))
				for user in users:
					try: user.send(f"[log] {username} подключен".encode('utf-8'))
					except: pass
				users.append(conn)
			else:
				if not msg:
					print(f"[log] {addr} отсоединился")
				else:
					print(f"[log] Сообщение от {addr}:", msg, f'\n[log] Отсоединяемся от {addr}')
				conn.close()

sock.close()
print("[log] Сервер остановлен")
