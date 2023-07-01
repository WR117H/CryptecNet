import threading
import socket
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--host', type=str, default='127.0.0.1', help='IP address of host for the chatroom ')
parser.add_argument('--port', type=int, default=9999, help='Port number of the host you wanna build tha chatroom on')

args = parser.parse_args()

port = args.port
ip_address = args.host

class ChatroomServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = None
        self.clients = {}

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Chatroom server started on {self.host}:{self.port}")

        while True:
            client_socket, client_address = self.server_socket.accept()
            username = client_socket.recv(1024).decode("utf-8")
            self.clients[client_socket] = username
            print(f"New client connected: {username}")

            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):
        username = self.clients[client_socket]

        while True:
            try:
                message = client_socket.recv(1024).decode("utf-8")
                if message:
                    self.broadcast(username, message, client_socket)
                else:
                    self.remove_client(client_socket)
                    break
            except Exception as e:
                print(f"Error: {e}")
                self.remove_client(client_socket)
                break

    def broadcast(self, sender_username, message, sender_socket):
        for client_socket, username in self.clients.items():
            if client_socket != sender_socket:
                try:
                    client_socket.sendall(f"{sender_username}: {message}".encode("utf-8"))
                except Exception as e:
                    print(f"Error broadcasting message: {e}")
                    self.remove_client(client_socket)

    def remove_client(self, client_socket):
        username = self.clients[client_socket]
        del self.clients[client_socket]
        client_socket.close()
        print(f"Client disconnected: {username}")

if __name__ == "__main__":


    server = ChatroomServer(ip_address, port)
    server.start()
