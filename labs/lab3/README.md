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
# will keep only 10 clients waitiing in the server queue. Additional requests when queue is full will be drooped. 
MAX_NUM_CONN = 10 
# bind ip address and port
serversocket.bind((host, port)) # (host, port) are passed as a parameter in a tuple. 
serversocket.listen(NAX_NUM_CONN) # server starts listening for client connections. 
```

4. Clients connections. When a client tries to connect to our server, it needs to be accepted first as part of the 
handshake process betweem them. Since servers are designed to accept multiple clients, they need to keep listening
for clients requests to connect. 

```python
client, addr = serversocket.accept() 
server_ip = addr[0]
client_id = addr[1] 
```

