"Management Techniques Compared"
# Two dynamically computed attributes with properties

class Powers(object):                           # Need(object) in 2.X only
    def __init__(self, square, cube):
        self._square = square                   # _square is the base value 
        self._cube   = cube                     # square is the property name
    
    def getSquare(self):
        return self._square ** 2
    def setSquare(self, value):
        self._square = value
    square = property(getSquare, setSquare)

    def getCube(self):
        return self._cube ** 3
    cube = property(getCube)


X = Powers(3, 4)
print(X.square)                 # 3 ** 2 = 9
print(X.cube)                   # 4 ** 3 = 64
X.square = 5
print(X.square)                 # 5 ** 2 = 25
print()


"""
To do the same with descriptors, we define the attributes with complete classes. Note
that these descriptors store base values as instance state, so they must use leading underscores
again so as not to clash with the names of descriptors; as we’ll see in the final
example of this chapter, we could avoid this renaming requirement by storing base
values as descriptor state instead, but that doesn’t as directly address data that must
vary per client class instance:
"""
# Same, but with descriptors (per-instance state)

class DescSquare(object):
    def __get__(self, instance, owner):
        return instance._square ** 2
    def __set__(self, instance, value):
        instance._square = value
    
class DescCube(object):
    def __get__(self, instance, owner):
        return instance._cube ** 3
    
class Powers(object):
    square = DescSquare()
    cube   = DescCube()
    def __init__(self, square, cube):
        self._square = square                               # "self.square" works too,
        self._cube   = cube                                 # because it triggers desc.__set__!
    

X = Powers(3, 4)
print(X.square)                 # 3 ** 2 = 9 
print(X.cube)                   # 4 ** 3 = 64
X.square = 5
print(X.square)                 # 5 ** 2 = 25
print()

"""
To achieve the same result with __getattr__ fetch interception, we again store base
values with underscore-prefixed names so that accesses to managed names are undefined
and thus invoke our method; we also need to code a __setattr__ to intercept
assignments, and take care to avoid its potential for looping:
"""
# Same, but with generic __getattr__ undefined attribute interception

class Powers:
    def __init__(self, square, cube):
        self._square = square 
        self._cube   = cube 
    
    def __getattr__(self, name):
        if name == 'square':
            return self._square ** 2
        elif name == 'cube':
            return self._cube ** 3
        else:
            raise TypeError('unknown attr:' + name)
    
    def __setattr__(self, name, value):
        if name == 'square':
            self.__dict__['square'] = value                     # Or use object
        else:
            self.__dict__[name] = value 


X = Powers(3, 4)
print(X.square)                 # 3 ** 2 = 9 
print(X.cube)                   # 4 ** 3 = 64
X.square = 5
print(X.square)                 # 5 ** 2 = 2
print()


"""
The final option, coding this with __getattribute__, is similar to the prior version.
Because we catch every attribute now, though, we must also route base value fetches
to a superclass to avoid looping or extra calls—fetching self._square directly works
too, but runs a second __getattribute__ call:
"""
# Same, but with generic __getattribute__ all attribute interception

class Powers(object):                                           # Need (object) in 2.X only
    def __init__(self, square, cube):
        self._square = square
        self._cube   = cube 
    
    def __getattribute__(self, name):
        if name == 'square':
            return object.__getattribute__(self, '_square') ** 2
        elif name == 'cube':
            return object.__getattribute__(self, '_cube') ** 3
        else:
            return object.__getattribute__(self, name)
        
    def __setattr__(self, name, value):
        if name == 'square':
            object.__setattr__(self, '_square', value)              # Or use __dict__
        else:
            object.__setattr__(self, name, value)


X = Powers(3, 4)
print(X.square)                 # 3 ** 2 = 9 
print(X.cube)                   # 4 ** 3 = 64
X.square = 5
print(X.square)                 # 5 ** 2 = 2
