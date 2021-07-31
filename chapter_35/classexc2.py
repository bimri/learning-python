"Coding Exceptions Classes"
class General(Exception): pass
class Specific1(General): pass
class Specific2(General): pass

def raiser0(): raise General()
def raiser1(): raise Specific1()
def raiser2(): raise Specific2()

for func in (raiser0, raiser1, raiser2):
    try:
        func() 
    except General as X:                                    # X us the raised instance
        print('caught: %s' % X.__class__)                   # Same as sys.exc_info()[0]


'''
Because __class__ can be used like this to determine the specific type of exception
raised, sys.exc_info is more useful for empty except clauses that do not otherwise have
a way to access the instance or its class.

Furthermore, more realistic programs usually
should not have to care about which specific exception was raised at all—by calling
methods of the exception class instance generically, we automatically dispatch to behavior
tailored for the exception raised.
'''
