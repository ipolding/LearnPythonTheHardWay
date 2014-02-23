class Scanner(object):

    def __init__(self):    
        self.direction_list = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
        self.verb_list = ['go','stop','kill','eat']
        self.stop_list = ['the','in','of','from','at','it']
        self.noun_list = ['door','bear','princess','cabinet']
        #self.number_list =  [0,1,2,3,4,5,6,7,8,9]
    
    def convert_number(self, s):
        try:
            return int(s)
        except ValueError:
            return None
    
    def scan(self, phrase):
    # This function needs to return a LIST of TUPLES
    # it needs to identify directions, verbs, nouns and errors
        words = phrase.lower().split()
        sentence = []
        for word in words:
            if word in self.direction_list:
                sentence.append(('direction', word))
            elif word in self.verb_list:
                sentence.append(('verb', word))
            elif word in self.stop_list:
                sentence.append(('stop', word))
            elif word in self.noun_list:
                sentence.append(('noun', word))
            elif self.convert_number(word):
                sentence.append(('number', self.convert_number(word)))
            else:
                sentence.append(('error', word))
        return sentence
