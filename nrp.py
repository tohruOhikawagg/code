import socket
import threading

class ResolutionServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connections = []
        self.lock = threading.Lock()
        self.running = False

    def start(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)
        print(f"Resolution server listening on {self.host}:{self.port}")
        self.running = True
        while self.running:
            try:
                client_socket, client_address = self.socket.accept()
                print(f"Connection from {client_address}")
                client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
                client_thread.start()
            except OSError as e:
                if self.running:
                    raise e

    def handle_client(self, client_socket):
        with self.lock:
            self.connections.append(client_socket)
        while True:
            data = client_socket.recv(1024)
            if not data:
                with self.lock:
                    self.connections.remove(client_socket)
                client_socket.close()
                break
            response = self.process_request(data)
            client_socket.send(response)

    def process_request(self, data):

        return b"Received"

    def stop(self):
        self.running = False
        self.socket.close()
        with self.lock:
            for connection in self.connections:
                connection.close()

class ResolutionServerManager:
    def __init__(self, servers):
        self.servers = servers

    def start_servers(self):
        for server in self.servers:
            server_thread = threading.Thread(target=server.start)
            server_thread.start()

    def stop_servers(self):
        for server in self.servers:
            server.stop()


class ResolutionClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))

    def send_request(self, request):
        self.socket.send(request)
        response = self.socket.recv(1024)
        return response

    def close(self):
        self.socket.close()


if __name__ == "__main__":
    servers = [
        ResolutionServer('127.0.0.1', 8080),
        ResolutionServer('127.0.0.1', 8081),
    ]

    manager = ResolutionServerManager(servers)
    manager.start_servers()

    for server in servers:
        client = ResolutionClient(server.host, server.port)
        response = client.send_request(b"Resolution Request")
        print(f"Response from server {server.port}: {response.decode()}")
        client.close()

    manager.stop_servers()
