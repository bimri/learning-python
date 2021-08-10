"Other Metaclass Coding Techniques"
'''
Although redefining the type superclass’s __new__ and __init__ methods is the most
common way to insert logic into the class object creation process with the metaclass
hook, other schemes are possible.
'''

'Using simple factory functions'
'''
For example, metaclasses need not really be classes at all. As we’ve learned, the class
statement issues a simple call to create a class at the conclusion of its processing. Because
of this, any callable object can in principle be used as a metaclass, provided it
accepts the arguments passed and returns an object compatible with the intended class.
In fact, a simple object factory function may serve just as well as a type subclass:
'''
# A simple function can serve as a metaclass too

def MetaFunc(classname, supers, classdict):
    print('In MetaFunc: ', classname, supers, classdict, sep='\n...')
    return type(classname, supers, classdict)


class Eggs:
    pass

print('making class')
class Spam(Eggs, metaclass=MetaFunc):                       # Run simple function at end
    data = 1                                                # Function returns class
    def meth(self, arg):
        return self.data + arg

print('making instance')
X = Spam()
print('data:', X.data, X.meth(2))


'''
When run, the function is called at the end of the declaring class statement, and it
returns the expected new class object. The function is simply catching the call that the
type object’s __call__ normally intercepts by default:
'''
