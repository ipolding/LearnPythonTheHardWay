#Assigning a string with a number replaced to the variable x
x = "There are %d types of people." % 10
# Assigning string to binary variable
binary = "binary"
# Assigning string to do_not variable
do_not = "don't"
# Assigning string with two string replacement to y variable
y = "Those who know %s and those who %s." % (binary, do_not)

#Printing the string assigned to x
print x
#Printing the string assigned to y
print y

#printing string x to antoher string
print "I said: %r." % x

#printing string y to antoher string
print "I also said: '%s'." % y

# assigning hilarious the boolean value false
hilarious = False
# assigning string including a replacement to a variable
joke_evaluation = "Isn't that joke so funny?! %r"

#printing varibale joke evaluation swapping in the boolean variable
print joke_evaluation % hilarious

#a sitring vriable
w = "This is the left side of..."
# another string variable
e = "a string with a right side."

longstring = w + e

#putting second string at end of first string
print longstring
