from nose.tools import *
from lexiconPackage import parser
from lexiconPackage import scanner
from lexiconPackage.parser import ParserError
from lexiconPackage.parser import Sentence


def test_peek():
    """ peek should return the first word from a list"""
    phrase = "bear eat the princess"
    thisScanner = scanner.Scanner()
    word_list = thisScanner.scan(phrase)
    assert_equal(parser.peek(word_list), ("noun"))
    word_list = []
    assert_equal(parser.peek(word_list), None)

def test_match():
    """ Match should return an expected word type of the first tuple in a list of word type:word tuples.
    Unexpected word types are discarded"""
    phrase = "bear eat the princess"
    thisScanner = scanner.Scanner()
    word_list = thisScanner.scan(phrase)
    assert_equal(parser.match(word_list, "noun"), ('noun', 'bear'))
    assert_equal(parser.match([], "verb"), None)
    assert_equal(parser.match(["asdfasf","asdf","ffssf"], "verb"), None)

def test_parse_verb():
    """should return a verb from a word list"""
    phrase = "the go"
    thisScanner = scanner.Scanner()
    word_list = thisScanner.scan(phrase)
    assert_equal(parser.parse_verb(word_list), ('verb', 'go'))

@raises(ParserError)
def test_parse_verb_raise_error():
    """should return a verb from a word list"""
    phrase = "the princess"
    thisScanner = scanner.Scanner()
    word_list = thisScanner.scan(phrase)
    assert_equal(parser.parse_verb(word_list), ('verb', 'go'))

def test_parse_object():
    """ should return an object word verb from a word list"""
    phrase = "the princess go"
    thisScanner = scanner.Scanner()
    word_list = thisScanner.scan(phrase)
    assert_equal(parser.parse_object(word_list), ('noun', 'princess'))

@raises(ParserError)
def test_parse_object_raise_error():
    """should return a verb from a word list"""
    phrase = "the go princess"
    thisScanner = scanner.Scanner()
    word_list = thisScanner.scan(phrase)
    parser.parse_object(word_list)

def test_parse_subject():
    """ should return a sentence with the subject word at the beginning"""
    phrase = "the go north princess"
    thisScanner = scanner.Scanner()
    word_list = thisScanner.scan(phrase)
    assert_equal(parser.parse_subject(word_list, ('noun','princess')).subject,"princess")

def test_parse_sentence():
    """ returns a sentence with either the player or noun as the subject"""
    phrase = "the go north"
    thisScanner = scanner.Scanner()
    word_list = thisScanner.scan(phrase)
    assert_equal(parser.parse_sentence(word_list).subject, "player")

    phrase = "the princess eat bear"
    word_list = thisScanner.scan(phrase)
    assert_equal(parser.parse_sentence(word_list).subject, "princess")

@raises(ParserError)
def test_parse_sentence():
    """ returns a sentence with either the player or noun as the subject"""
    phrase = "north go"
    thisScanner = scanner.Scanner()
    word_list = thisScanner.scan(phrase)
    parser.parse_sentence(word_list)