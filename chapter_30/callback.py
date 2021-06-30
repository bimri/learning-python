"Function Interfaces and Callback-Based Code"

class Callback:
    def __init__(self, color):                              # Function + state information
        self.color = color
    def __call__(self):                                     # Support calls with no arguments
        print('turn', self.color)


if __name__ == '__main__':
    from tkinter import Button
    # Handlers
    cb1 = Callback('blue')              # Remember blue
    cb2 = Callback('green')             # Remember green
    B1 = Button(command=cb1)            # Register handlers
    B2 = Button(command=cb2)

    # Events
    cb1()                               # Prints 'turn blue'
    cb2()                               # Prints 'turn green'


"""
many consider such classes to be the best way to retain state information in the
Python language. With OOP, the
state remembered is made explicit with attribute assignments. This is different than
other state retention techniques (e.g., global variables, enclosing function scope references,
and default mutable arguments), which rely on more limited or implicit behavior.
Moreover, the added structure and customization in classes goes beyond state retention.

closure equivalent:
    def callback(color):                    # Enclosing scope versus attrs
        def oncall():
            print('turn', color)
        return oncall
    
    cb3 = callback('yellow')                # Handler to be registered
    cb3()                                   # On event: prints 'turn yellow'


there are two other ways that Python programmers sometimes tie
information to a callback function like this. One option is to use default arguments in
lambda functions:
    cb4 = (lambda color='red': 'turn ' + color) # Defaults retain state too
    print(cb4())

The other is to use bound methods of a class. A bound method object is a kind of object that remembers both the
self instance and the referenced function.

class Callback:
    def __init__(self, color):                      # Class with state information
        self.color = color
    def changeColor(self):                          # A normal named method
        print('turn', self.color)
    
    cb1 = Callback('blue')
    cb2 = Callback('yellow')
    
    B1 = Button(command=cb1.changeColor)            # Bound method: reference, don't call
    B2 = Button(command=cb2.changeColor)            # Remembers function + self pair

In this case, when this button is later pressed it’s as if the GUI does this, which invokes
the instance’s changeColor method to process the object’s state information, instead of
the instance itself:
    cb1 = Callback('blue')
    obj = cb1.changeColor                           # Registered event handler
    obj()                                           # On event prints 'turn blue'
"""


'''
Because __call__ allows us to attach
state information to a callable object, it’s a natural implementation technique for a
function that must remember to call another function when called itself.
'''
