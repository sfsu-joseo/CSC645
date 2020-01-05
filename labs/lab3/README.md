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

