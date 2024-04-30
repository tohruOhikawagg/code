import socket
import threading

def handle_client(client_socket, address):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                print(f"Connection closed by {address}")
                break

            broadcast(data, client_socket)

        except Exception as e:
            print(f"Error handling client {address}: {e}")
            break

    client_socket.close()


def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except Exception as e:
                print(f"Error broadcasting message: {e}")


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 5000))

server_socket.listen()
print("Server listening on 127.0.0.1:5000")
clients = []


while True:
    client_socket, address = server_socket.accept()
    print(f"Accepted connection from {address}")
    clients.append(client_socket)

    client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
    client_thread.start()
