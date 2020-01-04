#######################################################################################
# File:             menu.py
# Author:           Jose Ortiz
# Purpose:          CSC645 Assigment #1 TCP socket programming
# Description:      Template Menu class. You are free to modify this
#                   file to meet your own needs. Additionally, you are
#                   free to drop this Menu class, and use a version of yours instead.
# Running:          This class is dependent of other classes.
# Usage :           menu = Menu() # creates object
#                   print(menu.get_menu()) # prints the menu
#                   data = menu.user_data() # captures the data entered by the user
#
########################################################################################

class Menu(object):

    def __init__(self):
        """
        Empty constractor. No need to implement.
        """
        pass

    def get_menu(self):
        """
        TODO: Inplement the following menu
        ****** TCP CHAT ******
        -----------------------
        Options Available:
        1. Get user list
        2. Sent a message
        3. Get my messages
        4. Create a new channel
        5. Chat in a channel with your friends
        6. Disconnect from server
        :return: a string representing the above menu.
        """
        menu = ""
        # TODO: implement your code here
        return menu

    def _option_selected(self):
        """
        TODO: takes the option selected by the user in the menu
        :return: the option selected.
        """
        option = 0
        # TODO: your code here.
        return option

    def user_data(self):
        """
        TODO: according to the option passed as a parameter, prepare the data that will be sent to the server.
        TODO: don't forget to add also the option to the data.
        :param option:
        :return: a python dictionary representing the data needed to be sent to the server
        """
        data = {}
        option = self._option_selected()
        if 1 <= option <= 6: # validates a valid option
           data['option'] = option
           # TODO: implement your code here
        return data




