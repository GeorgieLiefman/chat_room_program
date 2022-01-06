"""This program contains the classes used by the client in a multi-user online chat room.

The code possesses the classes and functions needed to send and receive messages over a network. 
The socket module is implemented to establish a user socket which can connect to a server. The threading
module is also used to allow each user to have their own individual threads running with the host. Thereby,
enabling them to communicate with the host regardless of other users."""

# Import socket and threading modules in the program
import socket as s, threading as t

# User input to allow users to choose the username they wish to be displayed in the chat room
username = input("Please input the username you would like to be known as: ")

# Initialises the user's socket
user_socket = s.socket(s.AF_INET, s.SOCK_STREAM)

class UserSocket:
    """The purpose of this class is to give the necessary properties and functions to create a
     socket which can connect to another server.

    This class allows for the creation of a user socket which will be used to connect and communicate
    with the server. This process allows them to join the chat room and communicate with other users
    via the host socket.

    Attributes:
        ip: A string which contains the IP address that will be used when connecting to the 
        host socket.
        port: An integer which contains the port number that will be used when connecting to the 
        host socket."""


    def __init__(self):
        """Initialises the properties of the class to create the user socket used in the chat room.

        The ip and port number properties provide the necessary address details needed for the client
        to connect to the server."""
        self.ip = "127.0.0.1"
        self.port_number = 65432
        

    def connect_to_server(self):   
        """Connects the user to the host server.
        
        The use of the inbuilt connect() function from the socket module allows the user to connect
        to the host and communicate with them once the connection has been established.

        Args:
            self: A variable which means the necessary properties for the user socket will 
            be inherited from the above __init__ method.""" 
        user_socket.connect((self.ip, self.port_number))   
        

class DataTransfers:
    """The purpose of this class is to contain the two functions which the user uses to both acquire
    and send information to the host.
    
    The functions in this class uses UTF-8 to both encode and decode any communication that a user 
    sends or receives from the server."""


    def acquire_information():
        """The purpose of this function is to receive messages from the server and create a username
        that will be used in the chat room.

        The function uses UTF-8 to both encode and decode any communication that a user sends or 
        receives from the server.
        
        Upon starting the program users will be prompted to input a username. Users then enter a 
        name which will be sent in an encoded message to the host. Once the host receives and decodes
        this communication, it will register the name and new user, allowing them to join the chat room.

        If a message is received from the server, the function will decode the message (which will have be 
        sent by another user in the chat) and display the communication in the terminal to the user. 

        Raises:
            An exception is raised whenever a socket error occurs. If this error does occur users will receive
            a print statement notifying them an error occurred while trying to communicate with the server and
            that their connection will be ceased. The socket will close after the user receives this print statement.

            A more general except clause is also added that will be raised if an error occurs which is not related
            to a socket error. Again users will receive a print statement informing them something has gone wrong
            and their connection will be closed. The socket will close after the user receives this print statement."""
        while True:                                                 
            try:
                communication = user_socket.recv(1024).decode("UTF-8")
                if communication == "USERNAME":
                    user_socket.send(username.encode("UTF-8"))
                else:
                    print(communication)
            except s.error:     
                print("There has been error when trying to communicate with the server! Your connection will now be closed.")
                user_socket.close()
                break   
            except:                                                 
                print("Something has gone wrong! Your connection will now be closed.")
                user_socket.close()
                break


    def send_information():
        """The purpose of this function is to send messages to the server.

            The function uses UTF-8 to encode any communication that a user dispatches to the server.

            The functions informs the design for how the message is displayed to the host and will be displayed
            to other users. Whatever the user inputs will be encoded before it is sent to the host."""
        while True:                                                 
            communication = "{}: {}".format(username, input(""))
            user_socket.send(communication.encode("UTF-8"))
            

class UserThreading:
    """The purpose of this class is to give the necessary properties and functions to enable threading between
   the host and user.
 
   Each user will have their own separate threads running with the host, allowing each user to independently
   acquire and transmit messages at any time regardless of what other users are doing.
  
   Attributes:
       acquire_text: A variable which contains the function which begins a separate thread for a user to
       accept messages from the host.
       compose_text: A variable which contains the function which begins a separate thread for a user to
       send messages to the host."""


    def __init__(self):
        """Initialises the properties of the class to create threading in the chat room.
 
       The variables contain the functions which create two threads for each user between them and the client.
       These threads relate to the sending and receiving of communications."""
        self.acquire_text = t.Thread(target=DataTransfers.acquire_information) 
        self.compose_text = t.Thread(target=DataTransfers.send_information) 
        