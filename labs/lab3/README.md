# LAB #3: TCP Server Socket. 

Please read this README file before class and use this as a reference during the lab session. 

In this lab, you will create a TCP Server socket. This socket accepts clients client connections, and provide services
to handle them in the server side. 

## Useful hints to follow in this lab 

### How to create a client socket. 

1. In order to create a server socket, first you need to import the socket library builtin in the standad Python libraries.
The socket library provides all the low level functions needed.

2. The following line of code creates a server socket. So, you can use that socket to call 
methods such as bind(), listen(), accept(), send(), recv()...

```python
import socket 
# creates the server socket 
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

3. Binding the server. Once the server socket is created, it needs to be bind to a ip address and port in order to 
start listening for other clients. 
```python
host = "127.0.0.1"
port = 12000
# will keep only 10 clients waitiing in the server queue. 
# Additional requests when queue is full will be drooped. 
MAX_NUM_CONN = 10 
# bind ip address and port
serversocket.bind((host, port)) # (host, port) are passed as a parameter in a tuple. 
serversocket.listen(NAX_NUM_CONN) # server starts listening for client connections. 
```

4. Clients connections. When a client tries to connect to our server, it needs to be accepted first as part of the 
handshake process between them. Since servers are designed to accept multiple clients, they need to keep listening
for clients requests to connect. Note that the following code is best suited in a loop to keep accepting clients.

```python
# server accepts a client trying to connect
# clienthandler is the handler of the client socket in server side. 
# it will share messages on behalf of the server with the original client socket. 
# addr contains server ip/port and client id assigned to the client
clienthandler, addr = serversocket.accept() 
server_ip = addr[0]
client_id = addr[1] 
```

5. Once the client is accepted, the server needs to acknowledge the connection to the client as a part of the 
handshake process. One way to accomplish this is by sending the assigned client id to the client. That way, the 
client assumes that since a valid client id has been assigned to it by the server, the connection was succesful

```python
import pickle 
data = {'clientid': client_id} 
serialezed_data = pickle.dumps(data) 
clienthandler.send(serialezed_data) # data sent to the client. 
```

6. Receiving data. The way the server receives data is similar to the client. However, in this case, 
the one receiving the data is the clienthandler. 
```python
MAX_ALLOC_MEM = 4096
# server receives data
data_from_client = clienthandler.recv(MAX_ALLOC_MEM) 
# deserializes the data received
serialized_data = pickle.loads(data_from_client) 
# do something with the data. 
```

7. When multiple clients are connected. How a clienthandler knows to which client send the data if the 
low level send() method does not provide a option to define the client recipient? Here is where your
CSC415 knowledge comes in handy. The clienthandler is a forked process from the client when it connects. 
Both of them share the same client id which basically is the pid of the process. Therfore, the clienthandler
related to a client process knows exactely where to send the message based on the pid. This is already 
implemented by the sockets library. So, you don't need to worry about this. 

