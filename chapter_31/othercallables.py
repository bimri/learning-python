"Other callables"
'''
In fact, bound methods are just one of a handful of callable object types in Python. As
the following demonstrates, simple functions coded with a def or lambda, instances that
inherit a __call__, and bound instance methods can all be treated and called the same
way:
'''

def square(arg):
    return arg ** 2                                         # Simple function (def or lambda)


class Sum:
    def __init__(self, val):                                # Callable instance
        self.val = val 
    def __call__(self, arg):
        return self.val + arg 
    

class Product:
    def __init__(self, val):                                # Bound methods
        self.val = val 
    def method(self, arg):
        return self.val * arg 
    

sobject = Sum(2)
pobject = Product(3)
actions = [square, sobject, pobject.method]                 # Function, instance, method

for act in actions:                                         # All three called same way
    print(act(5))                                           # Call any one-arg callable


print(actions[-1](5))                                       # Index, comprehensions, maps
print([act(5) for act in actions])
print(list(map(lambda act: act(5), actions)))


"""
Technically speaking, classes belong in the callable objects category too, but we normally
call them to generate instances rather than to do actual work—a single action is
better coded as a simple function than a class with a constructor, but the class here
serves to illustrate its callable nature:
"""
class Negate:
    def __init__(self, val):                                # Classes are callables too
        self.val = -val                                     # But called for object, not work
    def __repr__(self):                                     # Instance print format
        return str(self.val)
    

actions = [square, sobject, pobject.method, Negate]         # Call a class too
for act in actions:
    print(act(5))


print([act(5) for act in actions])                          # Runs __repr__ not __str__!

table = {act(5): act for act in actions}                    # 3.X/2.7 dict comprehension
for (key, value) in table.items():
    print('{0:2} => {1}'.format(key, value))                # 2.6+/3.X str.format
