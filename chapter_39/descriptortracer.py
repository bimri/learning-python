"Class Blunders I: Decorating Methods"
'Using descriptors to decorate methods'
'''
a descriptor is normally a class attribute
assigned to an object with a __get__ method run automatically whenever that attribute
is referenced and fetched; Descriptors may also have __set__ and __del__ access methods.

because the descriptor’s __get__ method receives both the descriptor class instance and 
subject class instance when invoked, it’s well suited to decorating methods when we need 
both the decorator’s state and the original class instance for dispatching calls.
'''
class tracer(object):                                           # A decorator+descriptor
    def __init__(self, func):                                   # On @ decorator
        self.calls = 0                                          # Save func for later call
        self.func = func
    def __call__(self, *args, **kwargs):                        # On call to original func
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)
    def __get__(self, instance, owner):                         # On method attribute fetch
        return wrapper(self, instance)
        # nested function and enclosing scope references to achieve the same effect
        # def wrapper(*args, **kwargs): # Retain both inst
        #     return self(instance, *args, **kwargs) # Runs __call__
        #     return wrapper


class wrapper:
    def __init__(self, desc, subj):                             # Save both instances
        self.desc = desc                                        # Route calls back to deco/desc
        self.subj = subj
    def __call__(self, *args, **kwargs):
        return self.desc(self.subj, *args, **kwargs)            # Runs tracer.__call__


def tracer(func):                                           # Use function, not class with __call__
    calls = 0                                               # Else "self" is decorator instance only!
    def onCall(*args, **kwargs):                            # Or in 2.X+3.X: use [onCall.calls += 1]
        nonlocal calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return onCall


class Person:
        def __init__(self, name, pay):
            self.name = name
            self.pay = pay
        @tracer
        def giveRaise(self, percent):                               
            self.pay *= (1.0 + percent)                             
        
        @tracer
        def lastName(self):
            return self.name.split()[-1]


if __name__ == '__main__':
    @tracer
    def spam(a, b, c):                  
        print(a + b + c)                
    @tracer
    def eggs(N):
        return 2 ** N
           
    print('methods...')
    bob = Person('Bob Smith', 50000)
    sue = Person('Sue Jones', 100000)
    print(bob.name, sue.name)
    sue.giveRaise(.10)                                              # Runs onCall(sue, .10)
    print(int(sue.pay))
    print(bob.lastName(), sue.lastName())                           # Runs onCall(bob), lastName in scopes


"""
This works the same as the preceding nested function coding. Its operation varies by
usage context:
    • Decorated functions invoke only its __call__, and never invoke its __get__.
    
    • Decorated methods invoke its __get__ first to resolve the method name fetch (on
    I.method); the object returned by __get__ retains the subject class instance and is
    then invoked to complete the call expression, thereby triggering the decorator’s
    __call__ (on ()).
"""
