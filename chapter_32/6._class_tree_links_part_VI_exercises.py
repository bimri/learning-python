""" 
6. Class tree links. In “Namespaces: The Whole Story” in Chapter 29 and in “Multiple
Inheritance: ‘Mix-in’ Classes” in Chapter 31, we learned that classes have a
__bases__ attribute that returns a tuple of their superclass objects (the ones listed
in parentheses in the class header). Use __bases__ to extend the lister.py mix-in
classes we wrote in Chapter 31 so that they print the names of the immediate
superclasses of the instance’s class. When you’re done, the first line of the string
representation should look like this (your address will almost certainly vary):
    <Instance of Sub(Super, Lister), address 7841200: 

"""
class ListInstance:
    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\t%s=%s\n' % (attr, self.__dict__[attr])
        return result
    
    def __str__(self):
        return '<Instance of %s(%s), address %s:\n%s>' % (
            self.__class__.__name__,                                                        # My class's name
            self.__supers(),                                                                # My class's own supers
            id(self),                                                                       # My address
            self.__attrnames())                                                             # name=value list
    
    def __supers(self):
        names = []
        for super in self.__class__.__bases__: # One level up from class
            names.append(super.__name__) # name, not str(super)
            return ', '.join(names)
            
            # Or: ', '.join(super.__name__ for super in self.__class__.__bases__)


if __name__ == "__main__":
    class Super:
        def __init__(self):
            self.data1 = 'spam'
    
    class Sub(Super, ListInstance):
        def __init__(self):
            Super.__init__(self)
            self.data2 = 'eggs'
            self.data3 = 42
    
    X = Sub()
    print(X)
    print(X.__dict__)
    print(X.__class__)
    print(X.__class__.__bases__)
    print(X.__class__.__bases__[0].__name__)
    print(X.__class__.__bases__[1].__name__)
    print(X.__class__.__bases__[1].__bases__[0].__name__)
