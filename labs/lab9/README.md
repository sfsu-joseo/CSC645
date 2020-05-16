# LAB 9: P2P Routing Table
In this lab, students will learn about the handling and routing concepts in a P2P network and why they are so important. In lab 8, students learned about the challenges found while implementing downloading mechanismes to download data from other peers. Two of the main challenges found when downloading data from other peers are the handleing and routing processes of that data 

## Routing Blocks 

Routing blocks is the process of routing pieces of data comming from different peers to the file they belong. This is a difficult process because those pieces of data may have been shared in different swarms. For example, P1, P2 and P3 are connected and sharing data in different swarms. When P1 receives data from P2, it needs a way of knowing to which file that piece of data belongs. The routing function is the one that perform this task. 

One way of implementing routing is to keep track of all the blocks that are being downloaded. So, for each block that is downloaded from a peer, the block is added to a routing table. The routing table will contain the following columns or keys:

```python
routing_table_entry = {'peer_id': 0, 'swarm_id': 0, 'client_id': client_id, 'piece_index': 0, 
                               'block_index': 0,  'block': block, 'flag': block_flag} 
```

## Your job in this lab 

In this lab, students will implement the basic functionality of the handling and routing functions in the Peer class. A template of the Peer class is provided in this lab, but you are free to replace it with your own Peer class from lab 8. 








