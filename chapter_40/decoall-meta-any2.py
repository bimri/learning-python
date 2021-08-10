"""
Now, to apply a different decorator to the methods, we can simply replace the decorator
name in the class header line. To use the timer function decorator shown earlier, for
example, we could use either of the last two header lines in the following when defining
our class—the first accepts the timer’s default arguments, and the second specifies label
text:
"""
class Person(metaclass=decorateAll(tracer)): ...                    # Apply tracer
class Person(metaclass=decorateAll(timer())): ...                   # Apply timer, defaults
class Person(metaclass=decorateAll(timer(label='**'))): ...         # Decorator arguments

'''
Notice that this scheme cannot support nondefault decorator arguments differing per
method in the client class, but it can pass in decorator arguments that apply to all such
methods
'''
