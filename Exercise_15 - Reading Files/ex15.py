#import the argv feature
from sys import argv

#ask for two command line arguments
script, filename = argv

# open the filename given in the command-line assign it the value txt
txt = open(filename)

#print out the filename given in the command-line argument
print "Here's your file %r:" % filename
#print the files contents

print txt.readline()

txt.close()

#ask for a string to be used as a filename (it must be in the same directory)
#print "Type the filename again:"
#file_again = raw_input("> ")

# open the file given above and assign it to the variable txt_again
#txt_again = open(file_again)

#read the file again
#print txt_again.read()
