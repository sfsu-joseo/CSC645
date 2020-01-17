# The Forwarding Protocol 

As you know from class material, the network layer is organized in two sublayers: the data and control planes. Data plane refers to all the functions and processes that forward packets/frames from one interface to another.

In this project students will implement the forwarding protocol. The following are the guidelines for this project: 

* Implement input and output queues located in the input and output interfaces of the router. Note that each interface has its own input and output queues or buffers. 

* Implement priority or robin round scheduling algorithms for the input and output buffers. 

* Implement ip fragmentation so the router fabric can forward datagrams to their correspondent interface 

* Implement ip matching to select the correct interface to which datagrams need to be forwarded. 

* Implement a basic functionality to avoid loosing packets so buffers in interfaces do not drop packets 

## User Input

The user should enter the following data when the program starts:

* The source and destination ip addresses 

* The number of interfaces in the router 

* The min and max range of ip addresses for all the interfaces in the router. 

* The number of bus lines in the router fabric 

* The MTU supported by each bus line in the router fabric 


