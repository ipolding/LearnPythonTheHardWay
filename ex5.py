name = 'Zed A. Shaw'
age = 35 # not a lie
height_in_inches = 74 # inches
cm_in_inch = 2.54
height_in_cm = height_in_inches * cm_in_inch
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height_in_cm
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %r depending on the coffee." % teeth

# This line is tricky, try to get it exactly right
print "If I add %r, %r, and %r I get %r." % (
    age, height_in_cm, weight, age + height_in_cm + weight)
