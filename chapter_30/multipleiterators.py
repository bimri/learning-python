"Multiple Iterators on One Object"
S = 'bimri'
for x in S:
    for y in S:
        print(x + y, end=' ')

"""
When we code user-defined iterables with classes, it’s up to us to decide whether we
will support a single active iteration or many. To achieve the multiple-iterator effect,
__iter__ simply needs to define a new stateful object for the iterator, instead of returning
self for each iterator request.
"""
