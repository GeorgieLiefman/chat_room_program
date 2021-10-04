"""This program contains the classes used by the server in a multi-user online chat room.

The code possesses the classes and functions needed to send and receive messages over a network. 
The socket module is implemented to establish a host socket which can connect to multiple users. The 
threading module is also used to allow the server to accept multiple clients at once."""

# Import socket and threading modules in the program
import socket as s, threading as t

# Initialises the host's socket
host_socket = s.socket(s.AF_INET, s.SOCK_STREAM)

class ServerSocket:
    """The purpose of this class is to give the necessary properties and functions to create a
    socket which can connect to multiple users.
 
    This class allows for the creation of a host socket which will be used to connect and communicate
    with clients. This process allows users to join the chat room and communicate with one another
    via the host socket.
 
    Attributes:
       ip: A string which contains the IP address that will be used when connecting to users.
       port: An integer which contains the port number that will be used when connecting to users."""

    def __init__(self):
        self.ip = "127.0.0.1"
        self.port_number = 65432
        """Initialises the properties of the class to create the host socket used in the chat room.

        The ip and port number properties provide the necessary address details for the server to accept
        users."""
        
    def start_server(self):    
        host_socket.bind((self.ip, self.port_number))                                               
        host_socket.listen()
        print("Server booted, please standby waiting for users to connect.")
        """Binds the host to an IP address and port and listens for new connections.

        By binding the host to the set IP address and port it makes it so the server will now only
        accept users on a certain IP address and PORT. After the socket is bound it then listens for 
        incoming connections. A print statement is executed to let the user know the server is running
        and waiting for clients to connect.
        
        Args:
            self: A variable which means the necessary properties for the server socket will
            be inherited from the above __init__ method."""



class UserInformationAndInteractions:
    """The purpose of this class is to give the necessary properties and functions to store user information
    and send/receive messages from the clients.

    The class uses UTF-8 to both encode and decode any communication that the server has with users. 

    Attributes:
        users: A list which will store the users who have joined the chat room.
        usernames: A list which will store the usernames of clients who have joined the chat room."""

    def __init__(self):
        self.users = []
        self.usernames = []
        """Initialises the properties of the class to create lists for user information.

            The lists will be appended each time a new client joins the chat room or if any client
            leaves or is disconnected from the server for whatever reason."""
    
    def relay_information(self, communication):                                                 
        for user in self.users:
            user.send(communication)
        """Sends texts to users in the list of users.

        The function transmits texts to all of the users found in the list of users.
        
        Args:
            self: A variable which means the necessary properties for the server socket will 
            be inherited from the above __init__ method.
            communication: A variable which is informed by a later function when users send a text
            to the server."""

    def manage_users(self, user):                                         
        while True:
            try:                                                            
                communication = user.recv(1024)
                self.relay_information(communication)
            except:                                                         
                guide = self.users.guide(user)
                self.users.remove(user)
                user.close()
                username = self.usernames[guide]
                self.relay_information("{} has exited the chat room.".format(username).encode('UTF-8'))
                self.usernames.remove(username)
                break
        """Dispatches and accepts texts from users and deletes users from the chat room.
 
        The function uses UTF-8 to encode any communication that the server has with users.
    
        The function receives texts sent by users and then uses the relay_information function to transmit
        the communication back to the users in the chat room.
        
        Args:
            self: A variable which means the necessary properties will be inherited from the above
            __init__ method.
            user: A variable which denotes a user's individual socket so it is known who is sending the message.
            
        Raises:
            An exception is raised when an error occurs for whatever reason. If an error does occur then
            the host deletes the user (who has raised an error) from the chat room. The user's socket is then
            closed and they are removed from both the user and username list. A message is also relayed
            to all users still in the user list informing them that a user (identified by their username)
            has left the chat room. This process is also followed if a user manually exits the chat room."""

    def accept_new_users(self):                                                          
        while True:
            user, identifier = host_socket.accept()
            print("A new user has joined on {}".format(str(identifier)))       
            user.send('USERNAME'.encode('UTF-8'))
            username = user.recv(1024).decode('UTF-8')
            self.usernames.append(username)
            self.users.append(user)
            print("For their username a new user has chosen {}".format(username))
            self.relay_information("{} has connected to the chat room!".format(username).encode('UTF-8'))
            user.send('\nYou have successfully joined the chat room.'.encode('UTF-8'))
            text = t.Thread(target=self.manage_users, args=(user,))
            text.start()
            """Accepts multiple new clients.
 
           The function uses UTF-8 to both decode and encode any communication that the server has with users.
 
           The function accepts multiple new clients through threading. Once a client has been accepted a
           print statement will be executed informing the host the address by which the new user has joined.
           The server will receive an encoded message from the user containing the username they have chosen
           to be known as for the chat. It will then decode the text it receives and a print statement will
           be executed informing the server the name they have chosen.
 
           The server will then inform all clients that a new user has joined the chat room and inform them of
           their chosen username. The new user will also receive a message from the host informing them they
           have successfully joined the chat room. A thread is also started to allow multiple new users to connect
           to the host despite what is occurring between other users and the host.
          
           Args:
               self: A variable which means the necessary properties will be inherited from the above
               __init__ method."""