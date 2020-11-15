import socket # для работы с сокетами

HOST = "127.0.0.1"
PORT = 5000
SERVER = (HOST, PORT)

# AF_INET == ipv4
# SOCK_DGRAM == UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # create a datagram socket

sock.sendto("Hi server!!!".encode('utf-8'), SERVER) # отправляем серверу закодированую сообщение

received_data, addr = sock.recvfrom(1024) # получаем информацию о сервере и его сообщение (max-1024 байта)
msg = received_data.decode('utf-8') # декодироваем сообщение
print(f"Message from Server: {msg}")
