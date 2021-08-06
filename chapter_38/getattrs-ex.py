"__getattr__ and __getattribute__"
'A First Example'

class Person:
    def __init__(self, name):                   # On [Person()]
        self._name = name                       # Triggers __setattr__!
    
    def __getattr__(self, attr):                # On [obj.undefined]
        print('get: ' + attr)
        if attr == 'name':                      # Intercept name: not stored
            return self._name                   # Does not loop: read attr
        else:
            raise AttributeError(attr)
    
    def __setattr__(self, attr, value):         # On [obj.any = value]
        print('set: ' + attr)
        if attr == 'name':
            attr = '_name'                      # Set internal name
        self.__dict__[attr] = value             # Avoid looping here
    
    def __delattr__(self, attr):                # On [del obj.any]
        print('del: ' + attr)
        if attr == 'name':
            attr = '_name'                      # Avoid looping here too
        del self.__dict__[attr]                 # but mucg less common
    

bmr = Person('Bimri Coder')             # bmr has a managed attribute
print(bmr.name)                         # Runs __getattr__
bmr.name = 'Coder Bimri'                # Runs __setattr__
print(bmr.name)
del bmr._name                           # Runs __delattr__

print('-'*20)
al = Person('Al Capone')                # al inherits property too
print(al.name)
# print(Person.name.__doc__)            # No equivalent here


"""
Notice that the attribute assignment in the __init__ constructor triggers __setattr__
too—this method catches every attribute assignment, even those anywhere within the
class itself. When this code is run, the same output is produced, but this time it’s the
result of Python’s normal operator overloading mechanism and our attribute interception
methods:

Also note that, unlike with properties and descriptors, there’s no direct notion of specifying
documentation for our attribute here; managed attributes exist within the code
of our interception methods, not as distinct objects.
"""


'Using __getattribute__'
# To achieve exactly the same results with __getattribute__, replace __getattr__
class Person:
    def __init__(self, name):                   
        self._name = name                       
    
    def __getattribute__(self, attr):                   # On [obj.any]
        print('get: ' + attr)
        if attr == 'name':                              # Intercept all names
            attr = '_name'                              # Map to internal name
        return object.__getattribute__(self, attr)      # Avoid looping here
    
    def __setattr__(self, attr, value):         
        print('set: ' + attr)
        if attr == 'name':
            attr = '_name'                      
        self.__dict__[attr] = value             
    
    def __delattr__(self, attr):               
        print('del: ' + attr)
        if attr == 'name':
            attr = '_name'
        del self.__dict__[attr]

print()
bmr = Person('Yuri Fyodor')             # bmr has a managed attribute
print(bmr.name)                         # Runs __getattr__
bmr.name = 'Neitzsche Friedrick'                # Runs __setattr__
print(bmr.name)
del bmr._name                           # Runs __delattr__

print('-'*20)
al = Person('Michio Kaku')                # al inherits property too
print(al.name)


"""
When run with this change, the output is similar, but we get an extra __getattri
bute__ call for the fetch in __setattr__ (the first time originating in __init__):
"""

'''
This example is equivalent to that coded for properties and descriptors, but it’s a bit
artificial, and it doesn’t really highlight these tools’ assets. Because they are generic,
__getattr__ and __getattribute__ are probably more commonly used in delegationbase
code (as sketched earlier), where attribute access is validated and routed to an
embedded object. Where just a single attribute must be managed, properties and descriptors
might do as well or better.
'''
