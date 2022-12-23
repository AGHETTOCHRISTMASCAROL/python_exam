import socket
import asyncio
import selectors

selector = selectors.DefaultSelector()

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 9999))
    server_socket.listen()
    selector.register(fileobj=server_socket, events=selectors.EVENT_READ, data=accept_connection)

def accept_connection(server_socket):
    client_socket, remote_address = server_socket.accept()
    print(f"[+] {remote_address}")
    selector.register(fileobj=client_socket, events=selectors.EVENT_READ, data=request_processing)

def request_processing(client_socket):
    client_message_b = client_socket.recv(1024)

    if not client_message_b:
        selector.unregister(fileobj=client_socket)
        client_socket.close()
    else:
        client_socket.send(client_message_b)

def main():
    while True:
        events = selector.select()
        for key, _ in events:
            callback = key.data
            callback(key.fileobj)

if __name__ == '__main__':
    server()
    main()