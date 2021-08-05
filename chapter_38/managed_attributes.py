"Managed Attributes"
'Especially for tools builders, managing attribute access can be an important'
'part of flexible APIs'
""" 
Moreover, an understanding of the descriptor model can make related tools such 
as slots and properties more tangible, and make even be required reading if it 
appears in code you must use.
"""

'Why Manage Attributes?'
'''
Object attributes are central to most Python programs—they are where we often store
information about the entities our scripts process. Normally, attributes are simply
names for objects; a person’s name attribute, for example, might be a simple string,
fetched and set with basic attribute syntax:
'''
# In most cases, the attribute lives in the object itself, or is inherited from a class 
# from which it derives.
class Person: pass 
Person.name                         # Fetch attribute value
Person.name = ValueError            # Change attribute value

"""
Suppose you’ve written a program to
use a name attribute directly, but then your requirements change—for example, you
decide that names should be validated with logic when set or mutated in some way
when fetched. It’s straightforward to code methods to manage access to the attribute’s
value (valid and transform are abstract here):
"""
class Person:
    def getName(self):
        if not valid():
            raise TypeError('cannot fetch name')
        else:
            return self.name.transform()
        
    def setName(self, value):
        if not valid(value):
            raise TypeError('cannot change name')
        else:
            self.name = transform(value)
        

person = Person()
person.getName()
person.setName('value')


'Inserting Code to Run on Attribute Access'
# A better solution would allow you to run code automatically on attribute access, if
# needed. That’s one of the main roles of managed attributes—they provide ways to add
# attribute accessor logic after the fact.
# More generally, they support arbitrary attribute
# usage modes that go beyond simple data storage.

"""
four accessor techniques:
    • The __getattr__ and __setattr__ methods, for routing undefined attribute fetches
    and all attribute assignments to generic handler methods.
    
    • The __getattribute__ method, for routing all attribute fetches to a generic handler
    method.
    
    • The property built-in, for routing specific attribute access to get and set handler
    functions.

    • The descriptor protocol, for routing specific attribute accesses to instances of classes
    with arbitrary get and set handler methods, and the basis for other tools such as
    properties and slots.
"""
