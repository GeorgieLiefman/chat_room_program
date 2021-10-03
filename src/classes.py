import socket as s, threading as t

server_socket = s.socket(s.AF_INET, s.SOCK_STREAM)

class Server:
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 65432
        
    def start_server(self):    
        server_socket.bind((self.host, self.port))                                               #binding host and port to socket
        server_socket.listen()


user_socket = s.socket(s.AF_INET, s.SOCK_STREAM)

class UserSocket:
    def __init__(self):
        self.ip = "127.0.0.1"
        self.port_number = 65432
        
    def connect_to_server(self):    
        user_socket.connect((self.ip, self.port_number))   


