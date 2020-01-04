# TCP Centralized Client-Server Network 

Please use this README file to provide the following documentation for this project:

* Your name and student id
* General description of the project (a few sentences)
* If you used external Python modules/libraries. Provide a requeriments.txt file  
* Python version and compatibility issues (if any). Your project must be run exactelly as in the running instructions described below in this file
* A few sentences about all the challenges you found during the implementation of this project and how you overcame them. Please be honest here. 

## Note that failure to provide the above docs will result in a 30% deduction in your final grade for this project. 

## Project Description:

A pdf file with all the detailed guidelines about this project can be found on iLearn. Here, we describe the most important features of this project.

The project goal is to create a basic server-client architecture network to provide basic functionalites/services to multiple clients. Those services are self explanatory in the following menu.  

```
****** TCP CHAT ******
-----------------------
Client id: 2345
Options Available:
1. Get user list
2. Sent a message
3. Get my messages
4. Create a new channel
5. Chat in a channel with your friends
6. Disconnect from server
```

The project template provided in this repository is a good starting point, and will save you a lot of time in the implementation of this project. There are some methods that are already implemented by the class instructor in the template. For those methods that are not implemented, they provide starting point instruction about how to implement them. Note: if you decide to use this template, implement code for the parts marked as TODO.

## Running the project, 

You must follow exactelly this instructions in order to run and test your project. If I cannot run your project, as the following guidelines state, you'll get a zero in this project no matter how much work have you put on it. So, test it properly before final submission. 

This project consist in two main entities, the server and the client. Server and client must be run in different machines located in the same LAN. (Local Area Network). There are other additional classes that must be in the following machines. 

the files client_handler.py, and menu.py must be located in the same directory as the server.py file. The file client_helper.py must be located in the same directory as the client.py file. 

Running the server: 

```
python server.py # python 2 version 
python3 server.py # python 3 version 
```





