"Example: Attribute Validations"
'Using Properties to Validate'

"""
To understand this code, it’s crucial to notice that the attribute assignments inside the
__init__ constructor method trigger property setter methods too. When this method
assigns to self.name, for example, it automatically invokes the setName method, which
transforms the value and assigns it to an instance attribute called __name so it won’t
clash with the property’s name.

This renaming (sometimes called name mangling) is necessary because properties use
common instance state and have none of their own. Data is stored in an attribute called
__name, and the attribute called name is always a property, not data.

names like __name are known as pseudoprivate attributes, and are changed
by Python to include the enclosing class’s name when stored in the instance’s namespace;
here, this helps keep the implementation-specific attributes distinct from others,
including that of the property that manages them.
"""
class CardHolder(object):                               # Need "(object)" for setter in 2.X
    acctlen = 8 
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct                                # Instance data
        self.name = name                                # These trigger prop setters too!
        self.age  = age                                 # __X mangled to have class name
        self.addr = addr                                # addr is not managed
                                                        # remain has no data 

    def getName(self):
        return self.__name    
    def setName(self, value):
        value = value.lower().replace(' ', '_')
        self.__name = value 
    name = property(getName, setName) 

    def getAge(self):
        return self.__age     
    def setAge(self, value):
        if value < 0 or value > 150:
            raise ValueError('invalid age')
        else:
            self.__age = value 
    age = property(getAge, setAge) 

    def getAcct(self):        
        return self.__acct[:-3] + '***'    
    def setAcct(self, value):
        value = value.replace('-', '')
        if len(value) != self.acctlen:
            raise TypeError('invalid acct number')
        else:
            self.__acct = value 
    acct = property(getAcct, setAcct)

    def remainGet(self):                                            # Could be a method, not attr
        return self.retireage - self.age                            # unless already using as attr
    remain = property(remainGet)

