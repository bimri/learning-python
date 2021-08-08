"Managing Functions and Classes Directly"
'''
Imagine, for example, that you require methods or classes used by an application to be
registered to an API for later processing (perhaps that API will call the objects later, in
response to events). Although you could provide a registration function to be called
manually after the objects are defined, decorators make your intent more explicit.

The following simple implementation of this idea defines a decorator that can be applied
to both functions and classes, to add the object to a dictionary-based registry.
Because it returns the object itself instead of a wrapper, it does not intercept later calls:
'''
# Registering decorated objects to an API
# from __future__ import print_function                               # 2.X

registry = {}
def register(obj):                                                  # Both class and func decorator
    registry[obj.__name__] = obj                                    # Add to registry
    return obj                                                      # Return obj itself, not a wrapper

@register
def spam(x):
    return(x ** 2)                                                  # spam = register(spam)

@register
def ham(x):
    return(x ** 3)

@register
class Eggs:                                                         # Eggs = resister(Eggs)
    def __init__(self, x):
        self.data = x ** 4 
    def __str__(self):
        return str(self.data)
    

print('Registry:')
for name in registry:
    print(name, '=>', registry[name], type(registry[name]))

print('\nManual calls:')
print(spam(2))                                                      # Invoke objects manually
print(ham(2))                                                       # Later calls not intercepted
X = Eggs(2)
print(X)

print('\nResistry calls:')
for name in registry:
    print(name, '=>', registry[name](2))                            # Invoke form registry
print()

'''
This example is artificial, but its technique is very general. For example, function decorators
might also be used to process function attributes, and class decorators might
insert new class attributes, or even new methods, dynamically.

A user interface might use this technique, for example, to register callback handlers for
user actions. Handlers might be registered by function or class name, as done here, or
decorator arguments could be used to specify the subject event; an extra def statement
enclosing our decorator could be used to retain such arguments for use on decoration.
'''


"""
Consider the following
function decorators—they assign function attributes to record information for later use
by an API, but they do not insert a wrapper layer to intercept later calls:
"""
# Augmenting decorated objects directly

def decorate(func):
    func.marked = True                      # Assign function attribute for later use 
    return func 

@decorate
def spam(a, b):
    return a + b 

print(spam.marked)


def annotate(text):                         # Same, but value is decorator argument
    def decorate(func):
        func.label = text 
        return func 
    return decorate

@annotate('spam data')
def spam(a, b):
    return a + b 

print(spam(1, 2), spam.label)


'''
Such decorators augment functions and classes directly, without catching later calls to
them.
'''
