# Routing Protocol: Link State (Control Plane) 5%

As you may know from class lectures, there are two routing algorithms that operate in the network layer, the link state and the distance vector protocols. The link state routing protocol is a routing algorithm that creates routing tables for all the routers in the network. Such routing tables contain the shortest path from source to destination. The distance vector routing algorithm updates the routing tables of all the routers in the network everytime a path in the network changes. In this extracredit assignment, students will implement the link state routing protocol.

## User Input 

This program needs the following data from the user: 

```shell script
   > python3 link_state_protocol.py
   > Enter the nodes in the network: x y u v w z
   > Enter the link costs: (x, y, 2) (x, v, 3) (x, z, 1) (z, v, 3) (z, w, 1) (z, u, 1) (v, y, 5) (v, w, 5) (y, w, 7) (u, w, 3) (u, y, 2)
```

## Program output 

The program output is the final routing table as follows:

```shell script
   Routing Table: 
   
   | destination |  path    | cost |
   -----------------------------------
   |      y      | (x,y)    |  2   |
   |      u      | (x,z,u)  |  2   |
   |      v      | (x,v)    |  3   |
   |      w      | (x,z,w)  |  2   |
   |      z      | (x,z)    |  1   |
   
```



