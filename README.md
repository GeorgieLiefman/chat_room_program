# <center>Chatroom Terminal Application<center> #

## <center>Application Features<center> ##
The program that has been created is a multi-user online chat room hosted on a server. The network communication functions via the use of sockets: one server socket and one or multiple client sockets. The program allows for clients to choose their own username and communicate with other users in a chatroom. Members of the chatroom will be informed via the server whenever a new client joins the application. All communication is encoded to be in UTF-8 before it is sent to either the client or server and then is decoded on the receiving end of the message.


## <center>Installation Instructions<center> ##
1. This application is written in Python 3 and it is assumed that users have it downloaded and installed on their computers. If not follow this link and the instructions to fulfill this requirement https://www.python.org/downloads/.

2. Both the socket and threading modules are used to run the chatroom application. Given both these modules are built-in modules in Python there will be no extra steps to install them on your machine.

## <center>Setup Instructions<center> ##
1. Download the code off Github onto your local machine.

2. Ensure all the necessary software and dependencies discussed in the installation instructions have been downloaded and are ready to go on your machine.

3. Navigate into the directory named ‘src’ via the terminal.

4. For the application to allow clients to join the chatroom a server has to be up and running. As such, for whichever machine shall be the server run the command 'python3 server.py' in the terminal to launch the server.

5. The server should now be booted and listening for incoming connections. In order to have a client join the chatroom, run the command 'python3 client.py' in the terminal on a different machine to where the server code is being run.

6. To have another client also join the chatroom run the same command in step 5 on another machine. This step can be repeated as many times as desired to have multiple clients in the chatroom.