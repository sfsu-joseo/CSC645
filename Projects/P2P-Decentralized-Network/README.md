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

# General Implementation Guidelines 

Note this are only high level guidelines. Your implementation will need to take into consideration more specific details to meet the minimum functionality/requirements in this app. 

1. Download the age.txt file and age.torrent file from ilearn 
2. Change the announce value of your age.torrent to the ip address of the machine where your first seeder will be run. 
3. Put the age.torrent file in the torrents folder of the project in all the machines you run a peer. 
4. Run your first peer: your first peer in the network is the announce and the first seeder in the network, then run the server and the tracker of this peer and finally wait for other peer connections. Once a peer connects, the server accepts the peer (if not chocked and the peer is interested) and then pass the request to the tracker. The tracker will add this peer to the list of peers connected to the network and then will broadcast this updated list to all the peers connected in the network. Note the seeder is just uploading data in this swarm. It does not download any data. However, a seeder may be a seeder in swarm X and a peer in swarm Y. Think about this because this concept is important......
5. Run the next peer in a different machine. This peer should scan the age.torrent file, extract the announce ip address, name of the file (age.txt) and check that this ip address is not the same as the one this peer is using, then, it should go the the shareable folder and check if it has the file age,txt. If the file is there, then this peer should automatically set its status to seeder. Otherwise, the status is kept as peer. In any of both cases, this peer connects to the announcer to get the list of ip_addresses connected to the network. If seeder, the seeder just run the server and the tracker and wait there for connections. If peer, then do step 6. 
6. If peer (not seeder nor announce) it connects to all the peers in the network running a client socket per connection. 
7. When a peer connects to another peer, after the initial handshake, the peer trying to connect sends to the other peer if it is interested or not, then the other peers send back a response with choked or non-choked, if not chocked then this peer sends its bitfield, the other peer will see which blocks are missing, and will wait for a request from this peer. Once this peer sends a requests asking for a block, the sharing process begins. 
8.  

# Submission Guidelines 

The due data of this project is on the last day of the semester for this class. After you complete and test your project, send an email to the class instructor jortizco@sfsu.edu with the link to the source code of your project in the master branch of your class repository 
the subject of the email must be: CSC545-01 Computer Networks: P2P Project Link
  
  
 


    


