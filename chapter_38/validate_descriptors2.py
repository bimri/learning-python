"Using Descriptors to validate"
'Option 2: Validating with per-client-instance state'

class CardHolder(object):                                           # Need all "(object)" in 2.X only
    acctlen = 8                                                     # Class data
    retireage = 59.5
    def __init__(self, acct, name, age, addr):
        self.acct = acct                                            # Client instance data
        self.name = name                                            # These trigger __set__ calls too!
        self.age = age                                              # __X needed: in client instance
        self.addr = addr                                            # addr is not managed
                                                                    # remain managed but has no data
    
    class Name(object):
        def __get__(self, instance, owner):                         # Class names: CardHolder locals
            return instance.__name
        def __set__(self, instance, value):
            value = value.lower().replace(' ', '_')
            instance.__name = value
    name = Name()                                                   # class.name vs mangled attr
    
    class Age(object):
        def __get__(self, instance, owner):
            return instance.__age                                   # Use descriptor data
        def __set__(self, instance, value):
            if value < 0 or value > 150:
                raise ValueError('invalid age')
            else:
                instance.__age = value
    age = Age()                                                     # class.age vs mangled attr
    
    class Acct(object):
        def __get__(self, instance, owner):
            return instance.__acct[:-3] + '***'
        def __set__(self, instance, value):
            value = value.replace('-', '')
            if len(value) != instance.acctlen:                      # Use instance class data
                raise TypeError('invald acct number')
            else:
                instance.__acct = value
    acct = Acct() # class.acct vs mangled name
    
    class Remain(object):
        def __get__(self, instance, owner):
            return instance.retireage - instance.age                # Triggers Age.__get__
        def __set__(self, instance, value):
            raise TypeError('cannot set remain')                    # Else set allowed here
    remain = Remain()



"""
One small caveat here: as coded, this version doesn’t support through-class descriptor
access, because such access passes a None to the instance argument (also notice the
attribute __X name mangling to _Name__name in the error message when the fetch attempt
is made):
    >>> from validate_descriptors1 import CardHolder
    >>> bob = CardHolder('1234-5678', 'Bob Smith', 40, '123 main st')
    >>> bob.name
    'bob_smith'
    >>> CardHolder.name
    'bob_smith'
    
    >>> from validate_descriptors2 import CardHolder
    >>> bob = CardHolder('1234-5678', 'Bob Smith', 40, '123 main st')
    >>> bob.name
    'bob_smith'
    >>> CardHolder.name
    AttributeError: 'NoneType' object has no attribute '_Name__name'

We could detect this with a minor amount of additional code to trigger the error more
explicitly, but there’s probably no point—because this version stores data in the client
instance, there’s no meaning to its descriptors unless they’re accompanied by a client
instance (much like a normal unbound instance method). In fact, that’s really the entire
point of this version’s change!
"""
