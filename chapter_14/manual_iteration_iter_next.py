f = open('script2.py')

print(f.__next__())                                         # Call iteration method directly
print(f.__next__())

# The next(f) built-in calls f.__next__() in 3.X
print(next(f))
print(next(f))
# print(next(f))

print()


L = [1, 2, 3]                                               # Obtain an iterator object from an iterable

I = iter(L)                                                 # Call iterator's next to advance to next item
print(
    I.__next__()
)

print(I.__next__())
print(I.__next__())
# print(I.__next__())                                      # StopIteration error


'''File Iters'''
f = open('script2.py')

print(
    iter(f) is f
)

print(
    iter(f) is f.__iter__()
)

print(f.__next__())


'''Lists and many other built-in objects, though, are not their own iterators because they
do support multiple open iterations'''
L = [1, 2, 3]
print( 
    iter(L) is L
)
# L.__next__()                    # AttributeError: 'list' object has no attribute '__next__'

I = iter(L)
print(
    I.__next__()
)

print(
    I.__next__()
)
