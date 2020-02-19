# Web Proxy Server

Note that this extracredit assignment is an addition to the TCP Client-Server project. This part of the assignment is optional. Students who implement this option will need to modify the main manu of their TCP Client-Server project. The new menu should look like the following one: 

```
****** TCP Client-Server Network ******
-----------------------
Options Available:
1. Get user list
2. Sent a message
3. Get my messages
4. Create a new chat room
5. Join an existing chat room
6. Turn web proxy server on
7. Disconnect from server
```

## Getting Started with the proxy server option (option 6 in the menu)

When users select this option, the server will turn on the web server proxy services and will show the following additional menu to the user. 

```
*** Proxy Server Settings *** 
1. Turn web caching On
2. Turn authentication On
3. Turn private browsing Off
4. Send a request (GET, HEAD OR POST): 
5. Turn web proxy server off

```

### Option 1. Turn web caching On. 
  
Once this option is selected, the user should be informed that the web caching option is on. Note how the next time the 
menu is loaded when this option is active, the option has changed to "turn web caching Off". 
  
```
Your option <enter a number>: 1
Web caching is on

*** Proxy Server Settings *** 
1. Turn web caching Off
2. Turn authentication On
3. Turn private browsing Off
4. Send a request (GET, HEAD OR POST): 
5. Turn web proxy server off
```
Once the web caching system is active in the proxy server, all the GET requests done in option 4, need to be cached. Every time we send a request to a server for the first time, the server should save the response in the cache folder. The name of the file should be a hashed identifier, and the extension of the file should be .pickle 

The following are examples of the names and extension of cached server responses. 

```
53d9b3a0-4c87-11ea-9d7f-784f4387efce.pickle
d54442c6-4c86-11ea-9d7f-784f4387efce.pickle
```
  
