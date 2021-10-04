"""This program contains the classes used by the client in a multi-user online chatroom.

The program contains the classes and functions needed to send and receive messages over a network. 
The socket module is implemented to establish a user socket which can connect to a server. The threading
module is also used to allow each user to have their own individuals threads running with the host. Thereby,
enabling them to communicate with the host regardless of other users."""

# Import socket and threading modules in the program
import socket as s, threading as t

# User input to allow users to choose the username they wish to be displayed in the chatroom
username = input("Please input the username you would like to be known as: ")

# Initalises the user's socket
user_socket = s.socket(s.AF_INET, s.SOCK_STREAM)

class UserSocket:
    """The purpose of this class is to give the necessary properites and functions to create a
     socket which can connect to another server.

    This class allows for the creation of a user socket which will be used to connect and communicate
    with the server. As such, allowing them to join the chatroom and communicate with other users
    via the host socket.

    Attributes:
        ip: A string which contains the IP adreess that will be used when connecting to the 
        host socket.
        port: An integer which contains the port number that will be used when connecting to the 
        host socket."""

    def __init__(self):
        self.ip = "127.0.0.1"
        self.port_number = 65432
        """Initilises the propeties of the class to create the user socket used in the chatroom.

        The ip and port number properties which provide the necessary address details for the client
        to the server."""
        
    def connect_to_server(self):    
        user_socket.connect((self.ip, self.port_number))   
        """Connects the user to the host server.
        
        The use of the inbuilt connect() function from the socket module allows the user to connect
        to the host and communicate with them once the connection has been established.

        Args:
            self: A varaible which means the necessary properties for the user socket will 
            be inherited from the above __init__ method.
        
        Returns:
            An established connection between the client and server."""



class DataTransfers:
    """The purpose of this class is to contain the two functions which the user uses to both accquire
    and send information to the host.
    
    The functions is this class uses UTF-8 to both encode and decode any communication that a user 
    sends or receives from the server."""

    def accquire_information():
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
        """The purpose of this function is to receive messages from the server and create a username
        that will be used in the chatroom.

        The functions uses UTF-8 to both encode and decode any communication that a user sends or 
        receives from the server.
        
        Upon connecting to the host users will be prompted to input a username. Users then enter a 
        name which will be sent in an encoded message to the host. Once the host recieves and decodes
        this communication, it will register the name and new user, allowing them to join the chatroom.

        If the message recieved from the server is not the intial message asking new users for a username
        then the function will decode the message (which will have be sent by another user in the chat) 
        and display the communication in the terminal to the user. 

        Returns:
            A decoded message from the server either asking them to enter a username thereby allowing them
            entry to the chatroom or a decoded message from other clients in the chat.

        Raises:
            An exception is raised whenever a socket error occurs. If this error does occur users will recieve
            a print statement notifying them an error occured while trying to communicate with the server and
            that their connectin will be ceased. The socket will close after the user recieves this print statement.

            A more general except clause is also added that will be raised if an error occurs which is not related
            to a socket error. Again users will recieve a print statement informing them something has gone wrong
            and their connection will be closed. The socket will close after the user recieves this print statement."""

    def send_information():
        while True:                                                 
            communication = "{}: {}".format(username, input(""))
            user_socket.send(communication.encode("UTF-8"))
            """The purpose of this function is to send messages to the server.

            The functions uses UTF-8 to encode any communication that a user dispatches to the server.

            The functions informs the design for how the message is displayed to the host and will be displayed
            to other users. Whatever the user inputs will be encoded before it is sent to the host.

            Returns:
                An encoded communication inputted by the user that will be sent to the host."""
            


class UserThreading:
    """The purpose of this class is to give the necessary properites and functions to enable threading between
    the host and user.

    Each user will have their own separate threads running with the host, allowing each user to independently
    accquire and transmit messages at anytime regardless of what other users are doing.
    
    Attributes:
        accquire_text: A variable which contains the function which begins a sesparate thread for a user to
        accept messages from the host.
        compose_text: A variable which contains the function which begins a sesparate thread for a user to
        send messages to the host."""

    def __init__(self):
        self.accquire_text = t.Thread(target=DataTransfers.accquire_information) 
        self.compose_text = t.Thread(target=DataTransfers.send_information) 
        """Initilises the propeties of the class to create threading in the chatroom.

        The variables contain the functions which create two threads for each user between them and the client.
        These threads relate to the sending and receiving of communications."""