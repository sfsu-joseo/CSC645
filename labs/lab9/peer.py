"""
Lab 9: Routing and Handing
Implement the routing and handling functions
"""
from server import Server # assumes server.py is in this directory.
from client import Client # assumes client.py is in this directory.
from tracker import Tracker # assumes tracker.py is this directory.

class Peer ():

    SERVER_PORT = 5000
    CLIENT_MIN_PORT_RANGE = 5001
    CLIENT_MAX_PORT_RANGE = 5010

    def __init__(self, server_ip_address):
        self.routing_table = []
    
    
    # Your code from lab 8 can be added here. 
        
    def get_block(client):
        """
        TODO: get a block 
        :param client: the client socket that is retrieving the block
        """
    
    def remove_piece_from_routing_table(piece_index):
        """
        TODO: deletes all the blocks of a piece from the routing table
              note that this method can be only called after the piece has
              been validated via hash
        :param piece_index: the piece index belonging to all the blocks that must be removed from the routing table
        return: VOID
        """
        pass # your code here 
    
    def is_piece_validated(piece):
        """
        TODO: validates a piece
              1. hash the piece passed as a parameter
              2. get the the piece in from the .torrent with the same index
              3. compare hashes
        :param piece the piece to be validated
        :return True if the piece is validated. Otherwise, returns false. 
        """
        pass # your code here
        
    def add_entry_to_routing_table(client_id, block):
        """
        TODO: Add this block to the routing table 
        :param client_id: the client id socket in charge of receiving this block. 
        :param block: the payload of the block (the actual data)
        :param block_flag: Set to 1 bit if this is the last block to complete the piece. Otherwise, set to 0 bit
        return: VOID
        """
        routing_table_entry = {'peer_id': 0, 'swarm_id': 0, 'client_id': client_id, 'piece_index': 0, 
                               'block_index': 0,  'block': block, 'flag': block_flag} 
        
        pass # your code here
