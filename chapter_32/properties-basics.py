"Properties: Attribute Accessors"
""" 
a property is a type of object assigned to a class attribute
name. You generate a property by calling the property built-in function, passing in up
to three accessor methods—handlers for get, set, and delete operations—as well as an
optional docstring for the property. If any argument is passed as None or omitted, that
operation is not supported.

The resulting property object is typically assigned to a name at the top level of a
class statement (e.g., name=property()), and a special @ syntax

When thus assigned, later accesses to the class property
name itself as an object attribute (e.g., obj.name) are automatically routed to one of the
accessor methods passed into the property call.
""" 
class operators: 
    def __getattr__(self, name): 
        if name == 'age':
            return 40 
        else:
            raise AttributeError(name) 
        
    
x = operators() 
print(x.age)                                            # Runs __getattr__

# AttributeError: name
# print(x.name)                                           # Runs __getattr__


""" 
For some coding tasks, properties can be less complex and quicker to run than the
traditional techniques. For example, when we add attribute assignment support, properties
become more attractive—there’s less code to type, and no extra method calls are
incurred for assignments to attributes we don’t wish to compute dynamically:
""" 
class properties(object):                               # Need object in 2.X for setters 
    def getage(self): 
        return 40 
    def setage(self, value): 
        print('set age: %s' % value) 
        self._age = value 
    age = property(getage, setage, None, None)


x = properties() 
print(x.age)                                            # Runs getage
x.age = 42                                              # Runs setage                     

print(x._age)                                           # Normal fetch: no getage call 
print(x.age)                                            # Runs getage 

x.job = 'trainer'                                       # Normal assign: no setage call
print(x.job)                                            # Normal fetch: no getage call


""" 
equivalent class based on operator overloading incurs extra method calls for assignments
to attributes not being managed and needs to route attribute assignments
through the attribute dictionary to avoid loops 
""" 
class operators:
    def __getattr__(self, name):                                    # On undefined reference 
        if name == 'age':
            return 40 
        else:
            raise AttributeError(name)

    def __setattr__(self, name, value):                             # On all assignments                        # On all assignments
        print('set %s %s' % (name, value))
        if name == 'age': 
            self.__dict__['_age'] = value                           # Or object.__setattr__()
        else:
            self.__dict__[name] = value                             # Or object.__setattr__()
        

x = operators()
print(x.age)                                                        # Runs __getattr__
x.age = 42                                                          # Runs __setattr__
print(x.age)                                                        

print(x._age)                                                       # Defined: no __getattr__ call
x.age = 42                                                          # Runs __getattr__
print(x.age)

x.job = 'trainer'                                                   # Runs __setattr__ again 
print(x.job)                                                        # Defined: no __getattr__ call
  

"code properties using the @ symbol function decorator syntax"  
class properties(object):                                            
    @property                                                       # Coding properties with decorators: ahead 
    def age(self):                                                  
        ... 
    @age.setter                                                     
    def age(self, value):
        ...

