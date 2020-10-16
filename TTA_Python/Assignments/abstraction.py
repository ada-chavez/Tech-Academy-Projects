##Python:     3.9.0
##
##Author:     Ada Chavez
##
##Purpose:    Deomonstrate abstraction in a class, create a child class that
##            defines the implementation of its parents abstract method, and to
##            create an object that utilizes both the parent and child methods.

from abc import ABC, abstractmethod

# abstract class
class consume(ABC):
    def drink(self):
        print("I am drinking water today.")
    # function passing an argument, but not saying how or what kind of data
    @abstractmethod
    def eat(self,appetizer):
        pass

# child class
class lunch(consume):

    def eat(self,appetizer):
        print('During lunch I am eating {} for my first course.'.format(appetizer))


# instantiating the child class lunch
obj2 = lunch()
obj2.drink()
obj2.eat('hummus and carrots')
