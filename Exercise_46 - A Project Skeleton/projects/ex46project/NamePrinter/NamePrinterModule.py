import re as re

class NamePrinter(object):
    
    def __init__(self):
        """ Initialises the three instance variables - welcome_message, users_name and name_print_message """
        self.welcome_message = "What's you're name punk?"
        self.users_name = None
        self.name_print_message = "Bonjour! "
        
    def ask_name(self):
        """ ask for the users name and assign it to an instance variable """
        self.users_name = raw_input(self.welcome_message)
        
    def print_name(self):
        """ print the users name """
        if self.users_name == None:
            print "You haven't told me your name!"
        else:
            print self.name_print_message + self.users_name
            
    def remove_regular_expression_from_name(self, regular_expression):
        """ Strip a regular expression from the users name """
        if self.users_name is not None:
            expression = re.compile(regular_expression)
            self.users_name = self.users_name + expression
        
