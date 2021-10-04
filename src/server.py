"""This program is the server code for a multi-user online chatroom.

The program uses the classes found in the server_classes file in order to function as expected.
The server accepts multiple new users through threading. For every new user the server will
add them and their chosen nickname to two seperate list. The host then receives messages from 
users and relays this information to all users in the user list."""

# Import the socket module and classes from the server_classes program
import socket as s     
from server_classes import ServerSocket
from server_classes import UserInformationAndInteractions                                   

# Initalises the server socket
host_socket = s.socket(s.AF_INET, s.SOCK_STREAM)

# Boot the server socket
boot_server = ServerSocket().start_server()

# Accept multiple users, receive communication from users and relay sent messages to users  
accept_communicate_with_clients = UserInformationAndInteractions().accept_new_users()

# Close the server socket  
host_socket.close()
print("The server session has ceased.")