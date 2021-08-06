"__getattr__ and __getattribute__"
'''
properties and descriptors—tools for managing specific attributes.
The __getattr__ and __getattribute__ operator overloading methods provide still
other ways to intercept attribute fetches for class instances. Like properties and descriptors,
they allow us to insert code to be run automatically when attributes are accessed.
As we’ll see, though, these two methods can also be used in more general ways.
Because they intercept arbitrary names, they apply in broader roles such as delegation,
but may also incur extra calls in some contexts, and are too dynamic to register in
dir results.

Attribute fetch interception comes in two flavors, coded with two different methods:
• __getattr__ is run for undefined attributes—because it is run only for attributes
not stored on an instance or inherited from one of its classes, its use is straightforward.
• __getattribute__ is run for every attribute—because it is all-inclusive, you must
be cautious when using this method to avoid recursive loops by passing attribute
accesses to a superclass.
'''

'The Basics'
def __getattr__(self, name): ...                        # On undefined attribute fetch [obj.name]
def __getattribute__(self, name): ...                   # On all attribute fetch [obj.name]
def __setattr__(self, name, value): ...                 # On all attribute assignment [obj.name=value]
def __delattr__(self, name): ...                        # On all attribute deletion [del obj.name]


class Catcher:
    def __getattr__(self, name):
        print('Get: %s' % name)
    def __setattr__(self, name, value):
        print('Set: %s %s' % (name, value))

X = Catcher()
X.job                                   # Prints "Get: job"
X.pay                                   # Prints "Get: pay"
X.pay = 99                              # Prints "Set: pay 99"


# __getattribute__ works exactly the same in this specific case
class Catcher(object):                                  # Need (object) in 2.X only
    def __getattribute__(self, name):                   # Works same as getattr here
        print('Get: %s' % name)                         # But prone to loops on general


'''
Because all attributes are routed to our interception methods
generically, we can validate and pass them along to embedded, managed objects.

There is no such analog for properties and descriptors, short of coding accessors for
every possible attribute in every possibly wrapped object.
'''
class Wrapper:
    def __init__(self, object):
        self.wrapped = object                           # Save object
    def __getattr__(self, attrname):
        print('Trace: ' + attrname)                     # Trace fetch
        return getattr(self.wrapped, attrname)          # Delegate fetch


X = Wrapper([1, 2, 3])
X.append(4)                                             # Prints "Trace: append"
print(X.wrapped)                                        # Prints "[1, 2, 3, 4]"


'Avoiding loops in attribute interception methods'
"""
These methods are generally straightforward to use; their only substantially complex
aspect is the potential for looping (a.k.a. recursing). Because __getattr__ is called for
undefined attributes only, it can freely fetch other attributes within its own code. However,
because __getattribute__ and __setattr__ are run for all attributes, their code
needs to be careful when accessing other attributes to avoid calling themselves again
and triggering a recursive loop.
"""
# def __getattribute__(self, name):
#     x = self.other                                                # LOOPS!


'''
Technically, this method is even more loop-prone than this may imply—a self attribute
reference run anywhere in a class that defines this method will trigger __getattri
bute__, and also has the potential to loop depending on the class’s logic. This is normally
desired behavior—intercepting every attribute fetch is this method’s purpose,
after all—but you should be aware that this method catches all attribute fetches wherever
they are coded. When coded within __getattribute__ itself, this almost always
causes a loop. To avoid this loop, route the fetch through a higher superclass instead
to skip this level’s version—because the object class is always a new-style superclass,
it serves well in this role:
'''
# def __getattribute__(self, name):
#     x = object.__getattribute__(self, 'other')                      # Force higher to avoid me


"""
For __setattr__, the situation is similar, as summarized in Chapter 30—assigning
any attribute inside this method triggers __setattr__ again and may create a similar
loop:
"""
# def __setattr__(self, name, value):
#     self.other = value                                              # Recurs (and might LOOP!)


"""
Here too, self attribute assignments anywhere in a class defining this method trigger
__setattr__ as well, though the potential for looping is much stronger when they show
up in __setattr__ itself. To work around this problem, you can assign the attribute as
a key in the instance’s __dict__ namespace dictionary instead. This avoids direct attribute
assignment:
"""
# def __setattr__(self, name, value):
#     self.__dict__['other'] = value                                  # Use attr dict to avoid me


"""
Although it’s a less traditional approach, __setattr__ can also pass its own attribute
assignments to a higher superclass to avoid looping, just like __getattribute__ (and
per the upcoming note, this scheme is sometimes preferred):
"""
# def __setattr__(self, name, value):
#     object.__setattr__(self, 'other', value)                        # Force higher to avoid me


"""
By contrast, though, we cannot use the __dict__ trick to avoid loops in __getattri
bute__:
"""
# def __getattribute__(self, name):
#     x = self.__dict__['other']                                      # Loops!

"""
Fetching the __dict__ attribute itself triggers __getattribute__ again, causing a recursive
loop. Strange but true!

The __delattr__ method is less commonly used in practice, but when it is, it is called
for every attribute deletion (just as __setattr__ is called for every attribute assignment).
When using this method, you must take care to avoid loops when deleting attributes,
by using the same techniques: namespace dictionaries operations or superclass method
calls.
"""
