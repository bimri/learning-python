'Simple looping statements won’t work here because this is not a linear iteration'

def sumtree(L):
    tot = 0 
    for x in L:                                         # For each item at this level
        if not isinstance(x, list):
            tot += x                                    # Add numbers directly
        else:
            tot += sumtree(x)                           # Recur for sublists
    return tot

L = [1, [2, [3, 4], 5], 6, [7, 8]]                      # Arbitrarily nested sublists
print(sumtree(L))

# Pathological cases
print(sumtree([1, [2, [3, [4, [5]]]]]))                 # Prints 15 (right-heavy)
print(sumtree([[[[[1], 2], 3], 4], 5]))                 # Prints 15 (left-heavy)


"Recursion versus queues and stacks"
'''
Python implements recursion by
pushing information on a call stack at each recursive call, so it remembers where it must
return and continue later

possible to implement recursive-style
procedures without recursive calls

using an explicit stack or queue of your own to
keep track of remaining steps
'''
# this code traverses the list in breadth-first fashion by levels
# forming a first-in-first-out queue.
def sumtree1(L):                                # Breadth-first, explicit queue
    tot = 0 
    items = list(L)                             # Start with copy of top level
    while items:
        front = items.pop(0)                    # Fetch/delete front item
        if not isinstance(front, list):
            tot += front                        # Add numbers directly
        else:
            items.extend(front)                 # <== Append all in nested list
    return tot 

# depth-first traversal
def sumtree2(L):                                # Depth-first, explicit stack
    tot = 0 
    items = list(L)                             # Start with copy of top level
    while items:                                
        front = items.pop(0)                    # Fetch/delete front item
        if not isinstance(front, list):
            tot += front                        # Add numbers directly
        else:
            items[:0] = front                   # <== Prepend all in nested list
    return tot

