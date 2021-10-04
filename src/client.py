"""This program is the client code for a multi-user online chat room.
 
The program uses the classes found in the client_classes file in order to function as expected.
The user enters their username for the chat room which is then sent to the host. Once they have
successfully joined the room they can talk to other users by sending texts to the server. The
host then relays the sent message to all users."""

# Import the socket module and classes from the server_classes program
import socket as s
from client_classes import UserSocket
from client_classes import UserThreading

# Initialises the user socket
run_user_socket = UserSocket().connect_to_server() 

# Starts a thread so the user can accept texts from the server sent by other users
import_communication = UserThreading().acquire_text.start()

# Starts a thread so the user can send texts via the host to other users
output_communication = UserThreading().compose_text.start()

