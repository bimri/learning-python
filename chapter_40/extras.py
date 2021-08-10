"The Downside of “Helper” Functions"
'''
metaclasses are often optional from a
theoretical perspective. We can usually achieve the same effect by passing class objects
through manager functions—sometimes known as helper functions—much as we can
achieve the goals of decorators by passing functions and instances through manager
code. Just like decorators, though, metaclasses:

    • Provide a more formal and explicit structure
    • Help ensure that application programmers won’t forget to augment their classes
    according to an API’s requirements
    • Avoid code redundancy and its associated maintenance costs by factoring class
    customization logic into a single location, the metaclass

'''


""" 
To illustrate, suppose we want to automatically insert a method into a set of classes.
Of course, we could do this with simple inheritance, if the subject method is known
when we code the classes. In that case, we can simply code the method in a superclass
and have all the classes in question inherit from it:
"""

class Extras:
    def extra(self, args):                              # Normal inheritance: too static
        ...
    
class Client1(Extras): ...                              # Clients inherit extra methods
class Client2(Extras): ...
class Client3(Extras): ...

X = Client1()                                           # Make an instance
X.extra(1)                                              # Run the extra methods


""" 
Sometimes, though, it’s impossible to predict such augmentation when classes are coded.
Consider the case where classes are augmented in response to choices made in a
user interface at runtime, or to specifications typed in a configuration file. Although
we could code every class in our imaginary set to manually check these, too, it’s a lot
to ask of clients (required is abstract here—it’s something to be filled in):
"""

def extra(self, arg): ...

class Client1: ...                                      # Client augments: too distributed
if required():
    Client1.extra = extra

class Client2: ...
if required():
    Client2.extra = extra 

class Client: ...
if required():
    Client3.extra = extra 


X = Client1()
X.extra()


"""
We can add methods to a class after the class statement like this because a class-level
method is just a function that is associated with a class and has a first argument to
receive the self instance. Although this works, it might become untenable for larger
method sets, and puts all the burden of augmentation on client classes (and assumes
they’ll remember to do this at all!).

It would be better from a maintenance perspective to isolate the choice logic in a single
place. We might encapsulate some of this extra work by routing classes through a
manager function—such a manager function would extend the class as required and
handle all the work of runtime testing and configuration:
"""
def extra(self, arg): ...

def extras(Class):                                      # Manager function: too manual
    if required():
        Class.extra = extra

class Client1: ...
extras(Client1)

class Client2: ...
extras(Client2)

class Client3: ...
extras(Client3)

X = Client1()
X.extra()


""" 
This code runs the class through a manager function immediately after it is created.
Although manager functions like this one can achieve our goal here, they still put a
fairly heavy burden on class coders, who must understand the requirements and adhere
to them in their code. It would be better if there was a simple way to enforce the augmentation
in the subject classes, so that they don’t need to deal with the augmentation
so explicitly, and would be less likely to forget to use it altogether. In other words, we’d
like to be able to insert some code to run automatically at the end of a class statement,
to augment the class.

This is exactly what metaclasses do—by declaring a metaclass, we tell Python to route
the creation of the class object to another class we provide:
"""

def extra(self, arg): ...

class Extras(type):
    def __init__(Class, classname, superclasses, attributedict):
        if required():
            Class.extra = extra


class Client1(metaclass=Extras): ...                    # Metaclass declaration only (3.X form)
class Client2(metaclass=Extras): ...                    # Client class is instance of meta
class Client3(metaclass=Extras): ...

X = Client1()                                           # X is instance of Client1
X.extra()


'''
Because Python invokes the metaclass automatically at the end of the class statement
when the new class is created, it can augment, register, or otherwise manage the class
as needed. Moreover, the only requirement for the client classes is that they declare the
metaclass; every class that does so will automatically acquire whatever augmentation
the metaclass provides, both now and in the future if the metaclass changes.
'''
