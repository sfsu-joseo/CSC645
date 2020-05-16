# LAB 9: P2P Routing Table
In this lab, students will learn about the handling and routing concepts in a P2P network and why they are so important. In lab 8, students learned about the challenges found while implementing downloading mechanismes to download data from other peers. Two of the main challenges found when downloading data from other peers are the handleing and routing processes of that data 

## Routing Blocks 

Routing blocks is the process of routing pieces of data comming from different peers to the file they belong. This is a difficult process because those pieces of data may have been shared in different swarms. For example, P1, P2 and P3 are connected and sharing data in different swarms. When P1 receives data from P2, it needs a way of knowing to which file that piece of data belongs. The routing function is the one that perform this task. 

One way of implementing routing is to keep track of all the blocks that are being downloaded. So, for each block that is downloaded from a peer, the block is added to a routing table. The routing table entry contains the following columns or keys:

```python
routing_table_entry = {'peer_id': 0, 'swarm_id': 0, 'client_id': client_id, 'piece_index': 0, 
                               'block_index': 0,  'block': block, 'flag': block_flag} 
```

## Your job in this lab 

1. Create a method get_block(client) that will retrieve a block from a peer 
2. If this block is not the last missing block for that specific piece, then create a routing table entry and add this block using the new entry to the routing table
3. If this block is the last missing block, after take all the blocks payloads belonging to that piece, create a hash of the piece, and validate the piece, once the piece is validated, then remove all the blocks entries from the routing table. 








