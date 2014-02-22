class ParserError(Exception):
    pass

class Sentence(object):

    def __init__(self, subject, verb, object):
        # remember we take ('noun', 'princess') tuples and convert them
        # i.e. we need to take the second word from the tuple
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = object[1]

def peek(word_list):
    """ Returns the first word from a word list """
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

def match(word_list, expecting):
    """ Removes first word from a word list, compares to expecting
    then returns or discards it """
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None

def skip(word_list, word_type):
    """ Removes any word without a recognisable type by calling match without using its result  """
    while peek(word_list) == word_type:
        match(word_list, word_type)

def parse_verb(word_list):
    """Returns a verb from a word list"""
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")


def parse_object(word_list):
    """ Returns an object word verb from a word list"""
    skip(word_list, 'stop')
    next = peek(word_list)

    if next == 'noun':
        return match(word_list, 'noun')
    if next == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or a direction next.")

def parse_subject(word_list, subj):
    """ Returns a sentence with the subject word at the beginning"""
    # We then identify the verb and the object
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(subj, verb, obj)

def parse_sentence(word_list):
    skip(word_list, 'stop')
    #get the first verb or noun which is the subject
    start = peek(word_list)

    if start == 'noun':
        subj = match(word_list, 'noun')
        return parse_subject(word_list, subj)

    elif start == 'verb':
        # assume the object is the player then
        return parse_subject(word_list, ('noun', 'player'))
    else:
        raise ParserError("Must start with subject, object, or verb not: %s" % start)