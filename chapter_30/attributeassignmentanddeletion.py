"Attribute Assignment and Deletion"
'''
the __setattr__ intercepts all attribute assignments. If this
method is defined or inherited, self.attr = value becomes self.__setattr__('attr',
value). Like __getattr__, this allows your class to catch attribute changes, and validate
or transform as desired.

If you wish to use this method, you can avoid loops by coding instance attribute assignments
as assignments to attribute dictionary keys. That is, use
self.__dict__['name'] = x, not self.name = x; because you’re not assigning to
__dict__ itself, this avoids the loop:
'''
class AccessControl:
    def __setattr__(self, attr, value):
        if attr == 'age':   
            self.__dict__[attr] = value + 10                # Not self.name=val or setattr
        else:
            raise AttributeError(attr + ' not allowed')
        

if __name__ == '__main__':
    X = AccessControl()
    X.age = 40 
    print(X.age)

    # X.name = 'Bob'                    # AttributeError: name not allowed


"""
A third attribute management method, __delattr__, is passed the attribute name string
and invoked on all attribute deletions (i.e., del object.attr). Like __setattr__, it must
avoid recursive loops by routing attribute deletions with the using class through
__dict__ or a superclass.

And for future reference, keep in mind that there are
other ways to manage attribute access in Python:
    • The __getattribute__ method intercepts all attribute fetches, not just those that
      are undefined, but when using it you must be more cautious than with __get
      attr__ to avoid loops.

    • The property built-in function allows us to associate methods with fetch and set
     operations on a specific class attribute.

    • Descriptors provide a protocol for associating __get__ and __set__ methods of a
      class with accesses to a specific class attribute.
      
    • Slots attributes are declared in classes but create implicit storage in each instance.
"""
