from server import Server 

class Tracker:
    def __init__(self, server_instance):
        self.server = server

    def add_peer_to_swarm(self, peer_id, peer_ip, peer_port):
        """
        TODO: when a peers connects to the network adds this peer
              to the list of peers connected
        :param peer_id:
        :param peer_ip:
        :param peer_port:
        :return:
        """
        pass # your code here

    def remove_peer_from_swarm(self, peer_id):
        """
        TODO: removes a peer from the swarm when it disconnects from the network
              Note: this method needs to handle exceptions when the peer disconnected abruptly without
              notifying the network (i.e internet connection dropped...)
        :param peer_id:
        :return:
        """
        pass # your code here

    def broadcast(self):
        """
        TODO: broadcast the list of connected peers to all the peers in the network.
        :return:
        """
        pass # your code here


