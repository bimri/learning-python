"Coding Function Decorators"
'Tracing Calls'

class tracer:
    def __init__(self, func):                           # On @decoration: save original func
        self.calls = 0
        self.func  = func 
    def __call__(self, *args):                          # On later calls: run original func
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        self.func(*args)
    

@tracer
def spam(a, b, c):                  # spam = tracer(spam)
    print(a + b + c)                # wraps spam in a decorator object


spam(56, 76.89, 87)
spam('b', 'i', 'm')                 # Invokes __call__ in class
c = spam.calls                      # Number calls in wrapper state information
print(c)
print(spam)
print()


"""
Notice how the total number of calls shows up as an attribute of the decorated function—spam is really
an instance of the tracer class when decorated, a finding that may have ramifications
for programs that do type checking, but is generally benign.

For function calls, the @ decoration syntax can be more convenient than modifying each
call to account for the extra logic level, and it avoids accidentally calling the original
function directly. Consider a nondecorator equivalent such as the following:
"""
calls = 0
def tracer(func, *args):
    global calls 
    calls +=1
    print('call %s to %s' % (calls, func.__name__))
    func(*args)

def spam(a, b, c):
    print(a, b, c)

spam(1, 3, 4)                           # Normal nontraced call: accidental?
tracer(spam, 1, 3, 4)                   # Special traced call without decorators
