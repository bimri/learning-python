"Why You Will Care: Bound Method Callbacks"
'''
Because bound methods automatically pair an instance with a class’s method function,
you can use them anywhere a simple function is expected. One of the most common
places you’ll see this idea put to work is in code that registers methods as event callback
handlers in the tkinter GUI interface
'''

from tkinter import Button
def handler():
    "...use globals or closure scopes for state..."
...
widget = Button(text='spam', command=handler)


'''
To register a handler for button click events, we usually pass a callable object that takes
no arguments to the command keyword argument. Function names (and lambdas) work
here, and so do class-level methods—though they must be bound methods if they expect
an instance when called:

Here, the event handler is self.handler—a bound method object that remembers both
self and MyGui.handler. Because self will refer to the original instance when handler
is later invoked on events, the method will have access to instance attributes that can
retain state between events, as well as class-level methods. With simple functions, state
normally must be retained in global variables or enclosing function scopes instead.
'''

class MyGui:
    def handler(self):
        "...use self.attr for state..."
    def makewidgets(self):
        b = Button(text='spam', command=self.handler)
     