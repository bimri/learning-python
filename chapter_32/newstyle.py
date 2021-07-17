"New Style Classes"
class C(object):                                        # New-style: 3.X and 2.X
    data = 'spam'   
    def __getattr__(self, name):                        # Catch normal names
        print('getattr: ' + name) 
        return getattr(self.data, name)
    def __getitem__(self, i):                           # Redefine built-ins
        print('getitem: ' + str(i)) 
        return self.data[i]
    def __add__(self, other):
        print('add: ' + other) 
        return getattr(self.data, '__add__')(other) 
    

if __name__ == '__main__':
    X = C()
    X.upper
    X.upper()
    X[1]                                                # Built-in operation(implicit) 
    X.__getitem__(1)                                    # Traditional equivalence (explicit)
    type(X).__getitem__(X, 1)                           # New-style equivalence

    X + 'eggs'                                          # Ditto for + and others
    X.__add__('eggs') 
    type(X).__add__(X, 'eggs') 

    "All Classes Derive from 'object'"
    class C: pass
    X = C() 
    type(X), type(C)                                    # Type is class instance was created from

    isinstance(X, object) 
    isinstance(C, object)                               # Classes always inherit from object

    type('spam'), type(str) 
    isinstance('spam', object)                          # Same for built-in types(classes) 
    isinstance(str, object)

    type(type)                                          # All classes are types, and vice versa 
    type(object) 

    isinstance(type, object)                            # Same for built-in types(classes)
    isinstance(object, type)                            # Types make classes, and type is a class

    type is object

    "Implications for defaults"
    print(dir(object))                                   # All attributes of object are inherited
    print(dir(type))                                     # All attributes of type are inherited

    class C: pass                                        # This means all classes get defaults in 3.X
    print(C.__bases__)                                   # Only new-style classes have __bases__

    X = C()
    print(C().__repr__)

