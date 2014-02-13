import re

class NamePrinter(object):
    """ NamePrinter has 3 functions: ask_user_for_name, print_name and remover_reg_ex_from_name """        
    def __init__(self):
        self.ask_name_phrase = "What's you're name punk?"
        self.users_name = None
        self.greeting = "Bonjour!"
         
    def ask_user_for_name(self):
        """ asks for the users name and assigns it to an instance variable users_name """
        self.users_name = raw_input(self.ask_name_phrase)
        
    def print_name(self):
        """ prints the users name """
        if self.users_name is not None:
            print self.greeting + self.users_name
        else:
            print "I don't know your name!"
            
    def remove_reg_ex_from_name(self, regex)            :
        pattern = re.compile(regex)
        self.users_name = pattern.sub('', self.users_name)
               
