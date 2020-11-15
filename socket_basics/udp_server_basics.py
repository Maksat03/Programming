import socket # для работы с сокетами

HOST = "127.0.0.1"
PORT = 5000

# AF_INET == ipv4
# SOCK_DGRAM == UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # create a datagram socket
sock.bind((HOST, PORT)) # привязать/свяжем сокет с данными хостом('127.0.0.1') и портом(5000)

received_data, addr = sock.recvfrom(1024) # получаем информацию о клиенте и его сообщение (max-1024 байта)
msg = received_data.decode('utf-8') # декодироваем сообщение

print('connected:', addr)
print(f"Message from Client: {msg}")

msg_to_client = "Hello client!!!"
sock.sendto(msg_to_client.encode('utf-8'), addr) # отправляем клиенту закодированую сообщение