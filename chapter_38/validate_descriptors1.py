"Using Descriptors to Validate"
'''
descriptors are very similar to properties in terms of functionality and roles; in fact,
properties are basically a restricted form of descriptor. Like properties, descriptors are
designed to handle specific attributes, not generic attribute access. Unlike properties,
descriptors can also have their own state, and are a more general scheme.
'''

'Option 1: Validating with shared descriptor instance state'
"""
notice that the attribute
assignments inside the __init__ constructor method trigger descriptor __set__ methods.
When the constructor method assigns to self.name, for example, it automatically
invokes the Name.__set__() method, which transforms the value and assigns it to a
descriptor attribute called name.

In the end, this class implements the same attributes as the prior version: it manages
attributes called name, age, and acct; allows the attribute addr to be accessed directly;
and provides a read-only attribute called remain that is entirely virtual and computed
on demand. Notice how we must catch assignments to the remain name in its descriptor
and raise an exception;
"""

class CardHolder(object):                                           # Need all "(object)" in 2.X
    acctlen = 8                                                     # class data
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct                                            # Instance data
        self.name = name                                            # These trigger __set__ calls too!
        self.age  = age                                             # __X not needed: in descritor
        self.addr = addr                                            # addr is not managed
                                                                    # remain has no data

    class Name(object):
        def __get__(self, instance, owner):                         # Class names: CardHolder locals
            return self.name 
        def __set__(self, instance, value):
            value = value.lower().replace(' ', '_')
            self.name = value 
    name = Name()

    class Age(object):
        def __get__(self, instance, owner):
            return self.age                                         # Use descritor data
        def __set__(self, instance, value):
            if value < 0 or value > 150:
                raise ValueError('invalid age')
            else:
                self.age = value 
    age = Age()

    class Acct(object):
        def __get__(self, instance, owner):
            return self.acct[:-3] + '***'
        def __set__(self, instance, value):
            value = value.replace('-', '')
            if len(value) != instance.acctlen:                      # Use instance class data
                raise TypeError('invald acct number')
            else:
                self.acct = value
    acct = Acct()

    class Remain(object):
        def __get__(self, instance, owner):
            return instance.retireage - instance.age # Triggers Age.__get__
        def __set__(self, instance, value):
            raise TypeError('cannot set remain') # Else set allowed here
    remain = Remain()

