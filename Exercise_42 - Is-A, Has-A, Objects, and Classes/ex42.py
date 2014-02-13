## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a animal and is-a object
class Dog(Animal):

    def __init__(self, name):
        ## dog has-a name
        self.name = name

## cat is-a animal
class Cat(Animal):

    def __init__(self, name):
        ## cat has-a name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a person is-a object
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic? Employee is initialise using person so its given a name
        super(Employee, self).__init__(name)
        ## employee also has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmin is-a fish
class Salmon(Fish):
    pass

## Halibut is-a fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is a cat has-a name satan
satan = Cat("Satan")

## mary is a person has-a name Mary
mary = Person("Mary")

## Mary has-a pet cat has-a name satan
mary.pet = satan

## frank is a Employee has-a Person's name Frank and a salary 120000
frank = Employee("Frank", 120000)

## frank has-a pet dog is-a animal has-a name rover
frank.pet = rover

## flipper is-a fish is-a object
flipper = Fish()

## crouse is-a salmon is-a fish
crouse = Salmon()

## harry is-a Halibut is-a fish
harry = Halibut()
