import socket # для работы с сокетами

HOST = '127.0.0.1'
PORT = 5000

# AF_INET == ipv4
# SOCK_STREAM == TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create the socket

sock.bind((HOST, PORT)) # привязать/свяжем сокет с данными хостом('127.0.0.1') и портом(5000)
sock.listen() # запустим для данного сокета режим прослушивания

conn, addr = sock.accept() # принимаем подключение. Ждем пока клиент не подключится к данному серверу/сокету

print('connected:', addr)

conn.settimeout(60) # установка таймаута. Теперь, если за 60 секунд не придут никакие данные, функция recv вернёт пустой объект bytes, как и при закрытом соединении.

received_data = conn.recv(1024) # принимаем макс-1024 байтовый сообщение от клиента

if not received_data:
	conn.close()

msg = received_data.decode('utf-8') # декодироваем сообщение
print(f"Message from Client: {msg}")

conn.send("HI, I am server!".encode('utf-8')) # отправляем клиенту закодированую сообщение

conn.close() # закрываем связь с клиентом
# sock.close() # Можно и закрыть сам сервер
