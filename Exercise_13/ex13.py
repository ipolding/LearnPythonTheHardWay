# imports allow you to add features to your script
# this feature comes from the sys module. Specifying what you're using helps documentation
# some programmers will call modules libraries
#argv holds values that you pass to the script when you run it
from sys import argv

script, first, second, third, fourth = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your fourth variable is:", fourth
