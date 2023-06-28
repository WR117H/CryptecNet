import socket
import time
import sys
import threading
import argparse
from colorama import Fore
from module import banner
parser = argparse.ArgumentParser(description='A script to make chatrooms with encryption')
parser.add_argument('--host', type=str, default='127.0.0.1', help='Host address to start the server on')
parser.add_argument('--port', type=int, default=9999, help='Port number of the chatroom server')
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
        if username == None:
           username = input("Enter your username: ")
           self.client_socket.sendall(username.encode("utf-8"))

        else:
           self.client_socket.sendall(username.encode("utf-8"))
        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.start()

        while True:
            message = input()

            if message.lower() == "/quit":
                self.client_socket.sendall(message.encode("utf-8"))
                self.client_socket.close()
                break


            else:

                self.client_socket.sendall(message.encode("utf-8"))

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode("utf-8")
                if message:
                    sender_username, _, message_content = message.partition(":")
                    if sender_username != "<You>":
                        print(message.replace("<You> ", ""))
            except Exception as e:
                print(f"Error receiving message: {e}")
                self.client_socket.close()
                break

if __name__ == "__main__":
   
    try:
       banner.ban()
       client = ChatroomClient(ip_address, port)
       client.start()
    except KeyboardInterrupt:
       print(Fore.LIGHTRED_EX+"[!] "+Fore.RESET+"Exiting . . .")
       time.sleep(3)
       sys.exit()
