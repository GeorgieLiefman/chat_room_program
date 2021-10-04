import socket as s, threading as t
from client_classes import UserSocket
from client_classes import DataTransfers
from client_classes import UserThreading


run_user_socket = UserSocket().connect_to_server() 
import_communication = UserThreading().accquire_text.start()
output_communication = UserThreading().compose_text.start()

