"Using __getattr__ to Validate"
'''
As for the property and descriptor versions of this example, it’s critical to notice that
the attribute assignments inside the __init__ constructor method trigger the class’s
__setattr__ method too. When this method assigns to self.name, for example, it automatically
invokes the __setattr__ method, which transforms the value and assigns
it to an instance attribute called name. By storing name on the instance, it ensures that
future accesses will not trigger __getattr__. In contrast, acct is stored as _acct, so that
later accesses to acct do invoke __getattr__.
'''

class CardHolder:
    acctlen = 8                                                     # Class data
    retireage = 59.5
    
    def __init__(self, acct, name, age, addr):
        self.acct = acct                                            # Instance data
        self.name = name                                            # These trigger __setattr__ too
        self.age = age                                              # _acct not mangled: name tested
        self.addr = addr                                            # addr is not managed
                                                                    # remain has no data
    
    def __getattr__(self, name):
        if name == 'acct':                                          # On undefined attr fetches
            return self._acct[:-3] + '***'                          # name, age, addr are defined
        elif name == 'remain':
            return self.retireage - self.age                        # Doesn't trigger __getattr__
        else:
            raise AttributeError(name)
    
    def __setattr__(self, name, value):
        if name == 'name':                                          # On all attr assignments
            value = value.lower().replace(' ', '_')                 # addr stored directly
        elif name == 'age':                                         # acct mangled to _acct
            if value < 0 or value > 150:
                 raise ValueError('invalid age')
        elif name == 'acct':
            name = '_acct'
            value = value.replace('-', '')
            if len(value) != self.acctlen:
                raise TypeError('invald acct number')
        elif name == 'remain':
            raise TypeError('cannot set remain')
        self.__dict__[name] = value                                 # Avoid looping (or via object)
