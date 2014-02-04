from nose.tools import *
from ex48 import lexicon

def test_directions():
    """ check scanning direction words returns correct tuples """
    assert_equal(lexicon.scan("north"), [('direction', 'north')})
    result = lexicon.scan("north south east")
    # check that scanning three words returns all three tuples
    assert_equal(result, [('direction', 'north'),
                          ('direction', 'south'),
                          ('direction','east')])
                          
def test_verbs():
    """ check scanning verbs returns correct tuples"""
    assert_equal(lexicon.scan("go"), [()])                          
    result = lexicon.scan("go kill eat")                
