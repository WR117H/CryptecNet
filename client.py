import socket
import threading
from module import banner
import argparse
from colorama import Fore

parser = argparse.ArgumentParser()
parser.add_argument('--host', type=str, default='127.0.0.1', help='Host address to connect to')
parser.add_argument('--port', type=int, default=9999, help='Port number of the host server')
parser.add_argument('--user', type=str, help='Username for the chatroom')

args = parser.parse_args()

username = args.user
port = args.port
ip_address = args.host

class ChatroomClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = None

    def start(self):
        global username
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))
        if username is None:
            username = input("Enter your username: ")
            self.client_socket.sendall(username.encode("utf-8"))
        else:
            self.client_socket.sendall(username.encode("utf-8"))
        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.start()

        while True:
            message = input()
            self.client_socket.sendall(message.encode("utf-8"))

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode("utf-8")
                if message:
                    sender_username, _, message_content = message.partition(":")
                    print(Fore.LIGHTBLUE_EX + sender_username + Fore.RESET + " > " + message_content)
            except Exception as e:
                print(f"Error receiving message: {e}")
                self.client_socket.close()
                break

if __name__ == "__main__":
    banner.ban(0)
    client = ChatroomClient(ip_address, port)
    client.start()
