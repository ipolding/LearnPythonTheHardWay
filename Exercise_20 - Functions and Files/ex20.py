# import module that lets you use command-line arguments
from sys import argv

# unpack the command line arguments into two values
script, input_file = argv

# function that reads the entire file
def print_all(f):
    print f.read()
    
# function that moves to first position in the file
def rewind(f):
    f.seek(0)
    
#prints the line count and then reads the line corresponding to that count
def print_a_line(line_count, f):
    print line_count, f.readline()
    
#opens the fie given in the command-line argument
current_file = open(input_file)

#prints a line then a new line
print "First let's print the whole file:\n"

#calls the print_all function which reads the entire file
print_all(current_file)

#prints a line
print "Now let's rewind, kind of like a tape."

#calls the rewind function which sets the position in the file to 0.
# this is the beginning of the file
rewind(current_file)

#prints a line
print "Let's print three lines:"

# sets the of the variable current line to 1
current_line = 1
#prints the number 1, then reads the first line in the file
print_a_line(current_line, current_file)

#add 1 to the current_line value
current_line += 1
# prints 2, then reads the next line
print_a_line(current_line, current_file)

# adds one again
current_line += 1
# prints 3, then reads the next line
print_a_line(current_line, current_file)
