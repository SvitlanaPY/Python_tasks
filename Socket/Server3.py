import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('localhost', 8089))

server_socket.listen(5)  # become a server socket, maximum 5 connections
print("Server is listening")

while True:
    client_socket, addr = server_socket.accept()
    print('Got connection from', addr)

    client_socket.send('You are connected. Thank you for connecting'.encode('utf-8'))
    data = client_socket.recv(2048)

    print(data.decode("utf-8"))
