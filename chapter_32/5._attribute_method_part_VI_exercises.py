""" 
5. Set objects. Experiment with the set class described in “Extending Types by Embedding”.
Run commands to do the following sorts of operations:
    a. Create two sets of integers, and compute their intersection and union by using
    & and | operator expressions.

    b. Create a set from a string, and experiment with indexing your set. Which
    methods in the class are called?

    c. Try iterating through the items in your string set using a for loop. Which
    methods run this time?

    d. Try computing the intersection and union of your string set and a simple
    Python string. Does it work?

    e. Now, extend your set by subclassing to handle arbitrarily many operands using
    the *args argument form. (Hint: see the function versions of these algorithms
    in Chapter 18.) Compute intersections and unions of multiple operands with
    your set subclass. How can you intersect three or more sets, given that & has
    only two sides?

    f. How would you go about emulating other list operations in the set class? (Hint:
    __add__ can catch concatenation, and __getattr__ can pass most named list
    method calls like append to the wrapped list.)

"""
from setwrapper import Set


class MultiSet(Set):
    """
    Inherits all Set names, but extends intersect and union to support
    multiple operands; note that "self" is still the first argument
    (stored in the *args argument now); also note that the inherited
    & and | operators call the new methods here with 2 arguments, but
    processing more than 2 requires a method call, not an expression;
    intersect doesn't remove duplicates here: the Set constructor does;
    """
    def intersect(self, *others):
        res = []
        for x in self:                                                          # Scan first sequence
            for other in others:                                                # For all other args
                if x not in other: break                                        # Item in each one?
            else:                                                               # No: break out of loop
                res.append(x)                                                   # Yes: add item to end of result
        return Set(res)
    
    def union(*args):                                                           # self is args[0]
        res = []
        for seq in args:                                                        # For all args
            for x in seq:                                                       # For all nodes
                if not x in res:
                    res.append(x)                                               # Add new items to result
        return Set(res)


# if __name__ == "__main__":
    # x = MultiSet([1, 2, 3, 4])
    # y = MultiSet([3, 4, 5])
    # z = MultiSet([0, 1, 2])
    # x & y, x | y                                    # Two operands    
    # x.intersect(y, z)                               # Three operands    
    # x.union(y, z)    
    # x.intersect([1,2,3], [2,3,4], [1,2,3])          # Four operands    
    # x.union(range(10))                              # Non-MultiSets work, too
