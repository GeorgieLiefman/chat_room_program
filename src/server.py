import socket as s, threading as t       
from server_classes import ServerSocket
from server_classes import UserInformationAndInteractions                                   

host_socket = s.socket(s.AF_INET, s.SOCK_STREAM)


boot_server = ServerSocket().start_server()



data = UserInformationAndInteractions()
data.accept_new_users()

host_socket.close()
print("The server session has ceased.")