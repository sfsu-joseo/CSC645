#######################################################################################
# File:             client_helper.py
# Author:           Jose Ortiz
# Purpose:          CSC645 Assigment #1 TCP socket programming
# Description:      Template Menu class. You are free to modify this
#                   file to meet your own needs. Additionally, you are
#                   free to drop this Menu class, and use a version of yours instead.
# Running:          This class is dependent of the client class
# Usage :           client_helper = ClientHelper(client) # creates object
#
########################################################################################
class ClientHelper(object):

    def __init__(self, client):
        """
        Class constructor
        :param client: the client object
        """
        self.client = client
        self.menu = None

    def show_menu(self):
        """
        TODO: 1. if self.menu is empty, send a request to server requesting the menu.
        TODO: 2. receive and process the response from server (menu object) and set the menu object to self.menu
        TODO: 3. print the menu in client console.
        :return: VOID
        """
        pass

    def process_user_data(self):
        """
        TODO: according to the option selected by the user, prepare the data that will be sent to the server.
        :param option:
        :return: VOID
        """
        data = {}
        option = self.option_selected()
        if 1 <= option <= 6: # validates a valid option
           # TODO: implement your code here
           # (i,e  algo: if option == 1, then data = self.menu.option1, then. send request to server with the data)
           pass

    def option_selected(self):
        """
        TODO: takes the option selected by the user in the menu
        :return: the option selected.
        """
        option = 0
        # TODO: your code here.
        return option











