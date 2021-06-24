class rec: pass

"start attaching attributes to the class by assigning names"
"to it completely outside of the original class statement:"
'''
When used this way, a class is roughly similar to a “struct” in C, or a
“record” in Pascal. It’s basically an object with field names attached to it
'''
rec.name = 'Bob'                                                # Just objects with attributes
rec.age = 40

# Notice that this works even though there are no instances of the class yet;
# classes are objects in their own right, even without instances.
'''
as long as we have a reference to a class, we can set or change its attributes
anytime we wish.
'''
print(rec.name)                                                 # Like a C struct or a record


x = rec()                                                       # Instances inherit class names
y = rec()

# they will obtain the attributes we attached to the class by inheritance:
print(
    x.name,
    y.name
)
'''
these instances have no attributes of their own; they simply fetch the name attribute
from the class object where it is stored.

If we do assign an attribute to an instance,
though, it creates (or changes) the attribute in that object, and no other—crucially,
attribute references kick off inheritance searches, but attribute assignments affect only
the objects in which the assignments are made.
'''
x.name = 'Sue'                                                  # But assignment changes x only
print(rec.name, x.name, y.name)

'''
the attributes of a namespace
object are usually implemented as dictionaries, and class inheritance trees are
just dictionaries with links to other dictionaries.
Normally, __dict__ literally is an instance’s attribute namespace.
'''
print(list(rec.__dict__.keys()))
print(list(name for name in rec.__dict__ if not name.startswith('__')))
print(list(x.__dict__.keys()))
print(list(y.__dict__.keys()))

print(x.name, x.__dict__['name'])                           # Attributes present here are dict keys
print(x.age)
# print(x.__dict__['age'])                                    # Indexing dict does not do inheritance


'''
To facilitate inheritance search on attribute fetches, each instance has a link to its class
that Python creates for us—it’s called __class__, if you want to inspect it:
'''
print(x.__class__)                                          # Instance to class link


'''
Classes also have a __bases__ attribute, which is a tuple of references to their superclass
objects
'''
print(rec.__base__)                                         # Class to superclasses link


'''
Classes and instances are just namespace objects, with attributes
created on the fly by assignment. Those assignments usually happen within the class
statements you code, but they can occur anywhere you have a reference to one of the
objects in the tree.

Even methods, normally created by a def nested in a class, can be created completely
independently of any class object.
'''
def uppername(obj):
    return obj.name.upper()                                    # Still needs a self argument (obj)

print(uppername(x))                                             # Call as a simple function

'''
If we assign this simple function to an attribute of our class, though, it becomes a
method, callable through any instance, as well as through the class name itself as long
as we pass in an instance manually—
'''
rec.method = uppername                                          # Now it's a class's method!

print(x.method())                                               # Run method to process x
print(y.method())                                               # Same, but pass y to self
print(rec.method(x))                                            # Can call through instance or class
