# types themselves are an object type in Python
# the type of an object is an object of type type

'''The practical application of this is that type
objects can be used for manual type comparisons in Python if statements'''
import types


t = type([1]) == type([])                       # Compare to type of another list
print(t)

t = type([1]) == list                           # Compare to list type name
print(t)

is_inst = isinstance([1], list)                 # Test if list or customization thereof
print(is_inst)


def f(): pass 
t = type(f) == types.FunctionType               # types has names for other types
print(t)
