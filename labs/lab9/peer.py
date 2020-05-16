"""
Lab 9: Routing and Handing
Implement the routing and handling functions
"""
from server import Server # assumes server.py is in the root directory.
from client import Client # assumes server.py is in the root directory.
from routing import Routing 

class Peer (Server):

    SERVER_PORT = 5000
    CLIENT_MIN_PORT_RANGE = 5001
    CLIENT_MAX_PORT_RANGE = 5010

    def __init__(self, server_ip_address):
        Server.__init__(server_ip_address, self.SERVER_PORT)
        self.routing_table = Routing()


    def run_server(self):
        """
        Already implemented. puts this peer to listen for connections requests from other peers
        :return: VOID
        """
        self.run()

    # Your code from lab 8 can be added here. 

    def routing(self, piece, file_id, swarm_id):
        """
        TODO: route a piece that was received by this peer, then add that piece to the routing table
        :param piece:
        :param file_id:
        :param swarm_id:
        :return:
        """
        pass # your code here
