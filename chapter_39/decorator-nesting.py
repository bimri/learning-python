"Decorator Nesting"
'''
Decorator syntax of this form:
    @A
    @B
    @C
    def f(...):
        ...

runs the same as the following:
    def f(...):
    ...
    f = A(B(C(f)))

If all the decorators insert wrappers, the net effect is that when the original function
name is called, three different layers of wrapping object logic will be invoked, to augment
the original function in three different ways. The last decorator listed is the first
applied, and is the most deeply nested when the original function name is later called.
'''

"""
Just as for functions, multiple class decorators result in multiple nested function calls,
and possibly multiple levels and steps of wrapper logic around instance creation calls.
For example, the following code:
    @spam
    @eggs
    class C:
        ...
    
    X = C()

is equivalent to the following:
    class C:
        ...
    C = spam(eggs(C))
    
    X = C()

Again, each decorator is free to return either the original class or an inserted wrapper
object. With wrappers, when an instance of the original C class is finally requested, the
call is redirected to the wrapping layer objects provided by both the spam and eggs
decorators, which may have arbitrarily different roles—they might trace and validate
attribute access, for example, and both steps would be run on later requests.

For instance, the following do-nothing decorators simply return the decorated function:
"""
def d1(F): return F
def d2(F): return F
def d3(F): return F

@d1
@d2
@d3
def func():                                 # func = d1(d2(d3(func)))
    print('spam')
func()                                      # Prints "spam"


"""
When decorators insert wrapper function objects, though, they may augment the original
function when called—the following concatenates to its result in the decorator
layers, as it runs the layers from inner to outer:
"""
def d1(F): return lambda: 'X' + F()
def d2(F): return lambda: 'Y' + F()
def d3(F): return lambda: 'Z' + F()

@d1
@d2
@d3
def func():                             # func = d1(d2(d3(func)))
    return 'spam'

print(func())                           # Prints "XYZspam"
