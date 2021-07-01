"Methods Are Objects: Bound or Unbound"
'''
Because a class’s methods can be accessed from an instance or a class, though, they actually come in two
flavors in Python:
    Unbound (class) method objects: no self
        Accessing a function attribute of a class by qualifying the class returns an unbound
        method object. To call the method, you must provide an instance object explicitly
        as the first argument. In Python 3.X, an unbound method is the same as a simple
        function and can be called through the class’s name; in 2.X it’s a distinct type and
        cannot be called without providing an instance.
    
    Bound (instance) method objects: self + function pairs
        Accessing a function attribute of a class by qualifying an instance returns a bound
        method object. Python automatically packages the instance with the function in
        the bound method object, so you don’t need to pass an instance to call the method.
'''


"""
When calling a bound method object, Python provides an instance for you automatically—
the instance used to create the bound method object.
"""

class Spam:
    def doit(self, message):
        print(message)
    

# bound method object is generated along the way just before the method call’s parentheses
obj1 = Spam()
obj1.doit('hello world')


"We can assign this bound method pair to another name and then call it as though it were a simple function:"
object1 = Spam()
x = object1.doit                # Bound method object: instance+function
x('naki bono')

"returns a bound method object that packages the instance (object1) with the method function (Spam.doit)"
object2 = Spam()
x = object2.doit                # Bound method: instance+function
x('habari dunia')                # Same effect as object2.doit('...')

"if we qualify the class to get to doit, we get back an unbound method object, which is simply a reference to the function object."
object3 = Spam()
t = Spam.doit                   # Unbound method object (a function in 3.X)
t(object3, 'howdy')             # Pass in instance (if the method expects one in 3.X)

"By extension, the same rules apply within a class’s method if we reference self attributes that refer to functions in the class."
# A self.method expression is a bound method object because self is an instance object:
class Eggs:
    def m1(self, n):
        print(n)
    def m2(self):
        x = self.m1             # Another bound method ogject
        x(42)                   # Looks like a simple function
    

Eggs().m2()                     # Prints 41


'''
Most of the time, you call methods immediately after fetching them with attribute
qualification, so you don’t always notice the method objects generated along the way.
But if you start writing code that calls objects generically, you need to be careful to treat
unbound methods specially—they normally require an explicit instance object to be
passed in.
'''
