import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('localhost', 8089))

while True:
    data = client_socket.recv(2048)
    print(data.decode('utf-8'))
    client_socket.send(input(":::").encode('utf-8'))
