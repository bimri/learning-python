"Function Decorator Basics"
'''
Because they also accept and return functions, the classmethod and property built-in
functions may be used as decorators in the same way
'''


class Methods(object):                                              # object needed in 2.X for property setters
    def imeth(self, x):                                             # Normal instance method: passed a self
        print([self, x])
    
    @staticmethod
    def smeth(x):                                                   # Static: no instance passed
        print([x])
    
    @classmethod
    def cmeth(cls, x):                                              # Class: gets class, not instance
        print([cls, x])
    
    @property                                                       # Property: computed on fetch
    def name(self):
        return 'Bob ' + self.__class__.__name__


if __name__ == "__main__":
    from bothmethods_decoratos import Methods
    obj = Methods() 
    obj.imeth(1) 
    obj.cmeth(3)
    print(obj.name)
