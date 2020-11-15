import socket # для работы с сокетами

HOST = '127.0.0.1'
PORT = 5000

# AF_INET == ipv4
# SOCK_STREAM == TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create the socket
sock.connect((HOST, PORT)) # подключаемся к серверу указывая адрес и порт сервера

sock.send('Hello server!'.encode('utf-8')) # отправляем серверу закодированную сообщение

received_data = sock.recv(1024) # принимаем макс-1024 байтовый сообщение от сервера

msg = received_data.decode('utf-8') # декодироваем сообщение
print(f"Message from Server: {msg}")

sock.close() # закрываем сокет
