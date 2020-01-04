# TCP Centralized Client-Server Network 

Please use this README file to provide the following documentation for this project:

* Your name and student id
* General description of the project (a few sentences)
* If you used external Python modules/libraries. Provide a requeriments.txt file  
* Python version and compatibility issues (if any). Your project must be run exactelly as in the running instructions described below in this file
* Attach screenshots or videos to this file to ilustrate how your program works for all the options in the menu. 
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

Option 1:



The project template provided in this repository is a good starting point, and will save you a lot of time in the implementation of this project. There are some methods that are already implemented by the class instructor in the template. For those methods that are not implemented, they provide starting point instruction about how to implement them. Note: if you decide to use this template, implement code for the parts marked as TODO.

You are not allowed to use any external python module/library other than the ones provided in the template. If I found out that you used additional libraries to complete the project without the instructor approval, you'll get a zero directly in the project.

You can implement this project either in both python 2 or 3 versions. However, you need to specify in the docs of this file which version you implemented. I will use this info to run your project with the appropiate commands.

## Project Template. 

This project template consist in five files that are described in detail below: 

* server.py 
  
  the server.py file implements the Server class. The server class is in charge of listening for clients requests. 

## Running the project, 

You must follow exactelly this instructions in order to run and test your project. If I cannot run your project, as the following guidelines state, you'll get a zero in this project no matter how much work have you put on it. So, test it properly before final submission. 

This project consist in two main entities, the server and the client. Server and client must be run in different machines located in the same LAN. (Local Area Network). There are other additional classes that must be in the following machines. 

The files client_handler.py, and menu.py must be located in the same directory as the server.py file. The file client_helper.py must be located in the same directory as the client.py file. 

Additionally, This program must be compatible with the following OS architectures: Linux, Windows and macOS


Open a terminal in machine X and navigate to the directory where server.py is located. Then execute the following commands:

```
python server.py # if python 2 version 
python3 server.py # if python 3 version 
```
Take note of the server ip address in the LAN, so you can connect your clients to the server. 

Open a terminal in machine Y and navigate to the directory where client.py is located. Then execute the following commands:

```
python client.py # if python 2 version 
python3 client.py # if python 3 version 
```
## Project Submission

The due date of this project will be announced on ilearn, in class and by email. Projects are due before class, and it will be considered submitted only and only when students sent an email to the instructor <jortizco@sfsu.edu> with the link to your project in your repository using in the following email format. You can use it as a templete for your email. 
```
To: <jortizco@sfsu.edu>
Subject: CSC645-01 Computer Network: Client-Server Network Project Submission 
Body message:

Hi Professor Ortiz, 

My Client-Server Network Project has been completed. Here is the link to the project:

link: <your link>

<your name>
<your student id>
<your github username>

```

Good luck!!!











