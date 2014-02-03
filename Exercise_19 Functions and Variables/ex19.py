# The variables in your function are not CONNECTED to the the variables in your script!

#defines a function that takes two numbers as arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
#prints first argument
    print "You have %d cheeses!" % cheese_count
#prints second argument  
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
#prints and adds a new line
    print "Get a blanket.\n"

    
print "We can just give the function numbers directly:"
# uses the values 20 and 30 in the function
cheese_and_crackers(20,30)

print "OR, we can use variables from our script:"
#assigns integers to variables
amount_of_cheese = 10
amount_of_crackers = 50

#gives the argument 10 and 50 to the function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#gives the argument 30 and 11 to the function
print "We can even do math inside too:"
cheese_and_crackers(10 + 20 , 5 + 6)

print "And we can combine the two, variables and math:"
#gives that arguments 110 and 1050 to the function
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def sayPoop(number_of_times):
    print "Poop "* number_of_times 
    
sayPoop(1)
sayPoop(2)
sayPoop(3)
sayPoop(4)
sayPoop(5)
sayPoop(6)
sayPoop(7)
sayPoop(8)
sayPoop(9)
sayPoop(10)

