class Parent(object):

    def override(self):
        print "PARENT override()"

    def implicit(self):
        print "PARENT implicit()"

    def altered(self):
        print "PARENT altered()"

class Child(Parent):

    #overrides the parent method. print 'CHILD override()'
    def override(self):
        print "CHILD override()"

    #alters the parent altered method. It prints its own line; prints parent line; prints its own line
    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()


dad.implicit()
#implicit inheritance. prints PARENT implicit()
son.implicit()

#prints PARENT override()
dad.override()
#explicitly overrides. prints CHILD override() 
son.override()

#print PARENT altered()
dad.altered()
#prints own line; parent line; own line. altered override
son.altered()
