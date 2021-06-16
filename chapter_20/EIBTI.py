'''
fundamental built-in tools such as range, map, dictionary
keys, and even files are now generators

don’t complicate your code with user-defined generators if 
they are not warranted. Especially for smaller programs and 
data sets

simple lists of results will suffice, will be easier to understand, will be
garbage-collected automatically, and may be produced quicker

Explicit is better than implicit == EIBTI

Always: keep it simple unless it must be complicated!
'''

# On the other hand: Space and time, conciseness, expressiveness
'''
there are specific use cases that generators can address well. They can
reduce memory footprint in some programs, reduce delays in others, and can occasionally
make the impossible possible.

for example, a program that must
produce all possible permutations of a nontrivial sequence.
'''
import math
print(
    math.factorial(10)
)

from permute import permute1, permute2
seq = list(range(10))

# the list builder pauses for 37 seconds on my computer to build a 3.6-millionitem list
p1 = permute1(seq)                                  # 37 seconds on a 2GHz quad-core machine
                                                    # Creates a list of 3.6M numbers
print(
    len(p1), p1[0], p1[1]
)        

# but the generator can begin returning results immediately
p2 = permute2(seq)                                  # Returns generator immediately
print(
    next(p2)                                        # And produces each result quickly on request                                             
)
print(next(p2))

p2 = list(permute2(seq))                            # About 28 seconds, though still impractical
print(p1 == p2)


math.factorial(50)
p3 = permute2(list(range(50)))
print(
    next(p3)                                        # permute1 is not an option here!
)


"yield results that are more variable and less obviously deterministic"
import random 

math.factorial(20)                                  # permute1 is not an option here
seq = list(range(20))

random.shuffle(seq)                                 # Shuffle sequence randomly first
p = permute2(seq)
next(p)
next(p)

random.shuffle(seq)
p = permute2(seq)
next(p)
next(p)


'''
Class-based
iterables can produce items on request too, and are far more explicit than the magic
objects and methods produced for generator functions and expressions.

Like comprehensions, generators
also offer an expressiveness and code economy that’s hard to resist if you understand
how they work
'''