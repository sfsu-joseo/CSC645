# P2P Decentralized Network 

Please use this README file to provide the following documentation for this project:

* Your name and student id
* General description of the project (a few sentences)
* If you used external Python modules/libraries. Provide a requeriments.txt file  
* Python version and compatibility issues (if any)
* Clear and specific instructions about how to run your project. If your project does not run or contains errors, you'll get a 0 in the project no matter how much work you put on it. So, test your code properly and make sure that it runs without errors.
* A few sentences about all the challenges you found during the implementation of this project and how you overcame them. Please be honest here. 

## Note that failure to provide the above docs will result in a 30% deduction in your final grade for this project. 

# Project Guidelines 

In this project, and using the knowledge gathered in the labs, you will build a decentralized P2P network using the BitTorrent Protocol. Recall that in a decentralized P2P network the peer is the client, server and tracker at the same time.

## Peer 

The peer class is the main class of this network. It must to have the following functionalities:

### Server Side 

  * Handling multiple peers connections at the same time

  * Uploading data to the swarm, so other peers can download that data 

  * Implementing tracker services: the server side of a peer, when connected by other peer for the first time, needs to update the list of ip addresses connected to the network, and broadcast it to all the peers in the network. 
  
### Client side 

  * Connect to other peers to download data from them ( connect to their server side )
  
  * Handeling clients running in different ports in the same machine 
  
  * Routing data 
  
### General 

  * Changing status ( i.e from peer to seeder ), and therfore, changing services provided. 
  
  * Being able to understand the Peer Wire Protocol which is in chargue of handling the communication and messages sent between peers 
  
  * Implementing scalability: being able to be connected to multiple swarms sharing multiple files at the same time. 
  
  * Persistency: if the peers is disconnected from the network, and then it reconnects, the data and its configuration in the network must be persistent. (i.e restarting the downloading process in the same point where it was left before desconnecting)
  
  * For testing purposes, each peer must be run in a different machine in the same Local Area Network (LAN)
  
# Grading Guidelines 

1. If your peer file does not run, you´ll get a zero in this project. 

2. Provide correct and complete documentation. Make sure to specify in your docs how to run your program and the Python version you used to implement it. 

3. Your project will be graded based on completness and correctness. For each services that is not implemented, you´ll get points deducted. 

4. No template is provided in this project since you can rehuse the client, server and peer classes from labs and other projects

# Submission Guidelines 

The due data of this project is on the last day of the semester for this class. After you complete and test your project, send an email to the class instructor jortizco@sfsu.edu with the link to the source code of your project in the master branch of your class repository 
the subject of the email must be: CSC545-01 Computer Networks: P2P Project Link
  
  
 


    


