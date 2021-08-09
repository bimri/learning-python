""" 
Class decorators: The Public/Private class decorators we wrote in module access2.
py in this chapter’s first case study example will add performance costs to
every attribute fetch in a decorated class. Although we could simply delete the @
decoration line to gain speed, we could also augment the decorator itself to check
the __debug__ switch and perform no wrapping at all when the –O Python flag is
passed on the command line—just as we did for the argument range-test decorators.
That way, we can speed our program without changing its source, via command-
line arguments (python –O main.py...). While we’re at it, we could also use
one of the mix-in superclass techniques we studied to catch a few built-in operations
in Python 3.X too. Code and test these two extensions.
""" 


"""
File access.py (3.X + 2.X)
Class decorator with Private and Public attribute declarations.
Controls external access to attributes stored on an instance, or
inherited by it from its classes in any fashion.

Private declares attribute names that cannot be fetched or assigned
outside the decorated class, and Public declares all the names that can.

Caveats: in 3.X catches built-ins coded in BuiltinMixins only (expand me);
as coded, Public may be less useful than Private for operator overloading.
"""

from access_builtins import BuiltinsMixin                                      # A partial set

traceME = False 
def trace(*args):
    if traceME: print('[' + ' '.join(map(str, args)) + ']')


def accessControl(failIf):
    def onDecorator(aClass):
        if not __debug__:
            return aClass
        else:
            class onInstance(BuiltinsMixin):
                def __init__(self, *args, **kargs):
                    self.__wrapped = aClass(*args, *kargs)
                
                def __getattr__(self, attr):
                    trace('get:', attr)
                    if failIf(attr):
                        raise TypeError('private attribute fetch: ' + attr)
                    else:
                        return getattr(self.__wrapped, attr)
                    
                def __setattr__(self, attr, value):
                    trace('set:', attr, value)
                    if attr == '_onInstance__wrapped':
                        self.__dict__[attr] = value
                    elif failIf(attr):
                        raise TypeError('private attribute change: ' + attr)
                    else:
                        setattr(self.__wrapped, attr, value)
            return onInstance
    return onDecorator


def Private(*attributes):
    return accessControl(failIf=(lambda attr: attr in attributes))

def Public(*attributes):
    return accessControl(failIf=(lambda attr: attr not in attributes))
