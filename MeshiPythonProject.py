import socket
import clientone, clienttwo

# import threading library
import threading

SERVER = socket.gethostbyname(socket.gethostname())


# the format in which encoding
# and decoding will occur
FORMAT = "utf-8"

# Create a new socket for
# the server
server = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)

# bind the address of the
# server to the socket
server.bind(("127.0.0.1",4468))

# Lists that will contains
# all the clients connected to
# the server and their names.

clients, clinames = [], []

# function to start the connection
# connection start
def startServer():
  print("The current IP of the server is: " + SERVER)
  server.listen(100)

  while True:
    connection, addr = server.accept()
    connection.send("Name".encode("utf-8"))

    name = connection.recv(2048).decode()

    clinames.append(name)
    clients.append(connection)

    print(f"The name of new client is :{name}")

    # client message to show the name of the client
    client_message(f"{name} has joined!".encode("utf-8"))

    connection.send('Connection to the chat server successful!'.encode("utf-8"))

    # Start the client connection thread
    t = threading.Thread(target=client_connection, args=(connection, addr))
    t.start()
    t = threading.Thread(target=client_message)
    t.start()
    print(f"Total number of active connections {threading.activeCount() - 1}")

# function to send messages between server and clients
def client_connection(connection, addr):
   print(f"The new connection added is {addr}")
   print("Welcome to the chat!")
   connected = True

   while connected:
     try:
       client_message= connection.recv(2048)
       print("Client says: ", client_message.decode("utf-8"))
       server_message= input("Server says: ")
       connection.send(server_message.encode("utf-8"))
     except:
         print("An Error")


#function that show all the messages
def client_message(server_message):
  for client in clients:
      client.send(server_message)

# call the method to start the chat server
startServer()
