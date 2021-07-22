""" 
1. Inheritance. Write a class called Adder that exports a method add(self, x, y) that
prints a “Not Implemented” message. Then, define two subclasses of Adder that
implement the add method:
    ListAdder
    With an add method that returns the concatenation of its two list arguments
    
    DictAdder
    With an add method that returns a new dictionary containing the items in both
    its two dictionary arguments (any definition of dictionary addition will do)
    Experiment by making instances of all three of your classes interactively and calling
    their add methods.

Now, extend your Adder superclass to save an object in the instance with a constructor
(e.g., assign self.data a list or a dictionary), and overload the + operator
with an __add__ method to automatically dispatch to your add methods (e.g., X +
Y triggers X.add(X.data,Y)). Where is the best place to put the constructors and
operator overloading methods (i.e., in which classes)? What sorts of objects can
you add to your class instances?

In practice, you might find it easier to code your add methods to accept just one
real argument (e.g., add(self,y)), and add that one argument to the instance’s
current data (e.g., self.data + y). Does this make more sense than passing two
arguments to add? Would you say this makes your classes more “object-oriented”?
""" 


class Adder:
    def add(self, x, y):
        print('Not Implemented!')
    
    def __init__(self, start=[]):
        self.data = start
    
    def __add__(self, other):                                           # Or in subclasses?
        return self.add(self.data, other)                               # Or return type?


class ListAdder(Adder):
    def add(self, x, y):
        return x + y


class DictAdder(Adder):
    def add(self, x, y):
        new = {}
        for k in x.keys(): new[k] = x[k]
        for k in y.keys(): new[k] = y[k]
        return new
    

if __name__ == "__main__":
    adder = ListAdder()
    print(adder.add([1, 2], [3, 4]))
    
    dict_adder = DictAdder()
    print(dict_adder.add({"a": 1}, {"b": 2}))

# Adder2
class Adder:
    def __init__(self, start=[]):
        self.data = start
    
    def __add__(self, other):                                           # Pass a single argument
        return self.add(other)                                          # The left side is in self
    
    def add(self, y):
        print('not implemented!')


class ListAdder(Adder):
    def add(self, y):
        return self.data + y


class DictAdder(Adder):
    def add(self, y):
        d = self.data.copy()                                            # Change to use self.data instead of x
        d.update(y)                                                     # Or "cheat" by using quicker built-ins
        return d
