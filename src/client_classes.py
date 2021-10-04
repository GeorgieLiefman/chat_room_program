import socket as s, threading as t

username = input("Please input the username you would like to be known as: ")
user_socket = s.socket(s.AF_INET, s.SOCK_STREAM)

class UserSocket:
    def __init__(self):
        self.ip = "127.0.0.1"
        self.port_number = 65432
        
    def connect_to_server(self):    
        user_socket.connect((self.ip, self.port_number))   

class DataTransfers:
    def accquire_information():
        while True:                                                 
            try:
                communication = user_socket.recv(1024).decode('UTF-8')
                if communication == 'USERNAME':
                    user_socket.send(username.encode('UTF-8'))
                else:
                    print(communication)
            except:                                                 
                print("Something has gone wrong! Your connection will now be closed.")
                user_socket.close()
                break
    def send_information():
        while True:                                                 
            communication = '{}: {}'.format(username, input(''))
            user_socket.send(communication.encode('UTF-8'))

class UserThreading:
    def __init__(self):
        self.accquire_text = t.Thread(target=DataTransfers.accquire_information) 
        self.compose_text = t.Thread(target=DataTransfers.send_information) 