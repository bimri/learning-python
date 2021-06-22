"Namespace Dictionaries: __dict__"
import module2

print(
    list(module2.__dict__.keys())
)

print(
    list(name for name in module2.__dict__.keys() if not name.startswith('__'))
)

print(
    list(name for name in module2.__dict__ if not name.startswith('__'))
)


'''
This time we’re filtering with a generator instead of a list comprehension, and can omit
the .keys() because dictionaries generate their keys automatically though implicitly;
the effect is the same.
'''

# attribute fetch is similar to dictionary indexing
print(module2.name)
print(module2.__dict__['name'])
