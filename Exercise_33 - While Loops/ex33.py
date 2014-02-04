t = 0
numbers = []

def print_loads_of_numbers(i, increment, rangesize):
    for i in range(0, rangesize):
        print "At the top is %d" % i
        numbers.append(i)
        
        i = i + increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
    
    
print "The numbers: "

for num in numbers:
    print num        
   
print_loads_of_numbers(t, 3, 21)   
