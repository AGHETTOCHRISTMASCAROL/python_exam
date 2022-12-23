import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 9999))

while True:
    client_socket.send(input("[C] Ваше сообщение: ").encode())
    server_response = client_socket.recv(1024).decode()
    print(f"[C] Ответ Сервера: {server_response}\n")