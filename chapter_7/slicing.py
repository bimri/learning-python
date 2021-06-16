S = 'hello'
print(S[::-1])              # Reversing items


'''With a negative stride, the meanings 
of the first two bounds are essentially reversed.'''
s = 'abcedfg'
print(s[5:1:-1])                   # Bounds roles differ


'''slicing is equivalent to indexing with a slice
object'''
print('spam'[1:3])                  # slicing syntax
print('spam'[slice(1, 3)])          # Slice objs with inx syntax + object 
print('spam'[::-1])
print('spam'[slice(None, None, -1)])
