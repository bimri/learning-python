"Indexing and Slicing: __getitem__ and __setitem__"
"""
the __getitem__ method is called automatically for instance-indexing operations
When an instance X appears in an indexing
expression like X[i], Python calls the __getitem__ method inherited by the instance,
passing X to the first argument and the index in brackets to the second argument.
"""

class Indexer:
    def __getitem__(self, index):
        return index ** 2 
    
  

"__getitem__ is also called for slice expressions—"
'''
Really, though, slicing bounds are bundled up into a slice object and passed to the list’s
implementation of indexing. In fact, you can always pass a slice object manually—slice
syntax is mostly syntactic sugar for indexing with a slice object:
'''
L = [5, 6, 7, 8, 9]

def tester():
    X = Indexer()
    print(X[2])                                         # X[i] calls X.__getitem__(i)
    for i in range(5):
        print(X[i], end=' ')                            # Runs __getitem__(X, i) each time
    
    print()

    print(L[2:4])
    print(L[1:])
    print(L[:-1])
    print(L[::2])

    print()
    # Slice with slice objects
    print(L[slice(2, 4)])
    print(L[slice(1, None)])
    print(L[slice(None, -1)])
    print(L[slice(None, None, 2)])
    print()
    print()
    

if __name__ == '__main__':
    tester()


'''
Our previous class won’t handle slicing because its math assumes integer indexes are passed, but the
following class will. When called for indexing, the argument is an integer as before:
'''
class Indexer2:
    data = [5, 6, 7, 8, 9]
    def __getitem__(self, index):                               # Called fro index or slice
        print('getitem:', index)
        return self.data[index]                                 # Perform index or slice
    

def tester2():
    X = Indexer2()
    print(X[0])                                                        # Indexing sends __getitem__ ab integer
    print(X[1])
    print(X[-1])
    print()

    # Slicing sends __getitem__ a slice object
    print(X[2:4])
    print(X[1:])
    print(X[:-1])
    print(X[::2])
    print()
    print()


if __name__ == '__main__':
    tester2()


'''
Where needed, __getitem__ can test the type of its argument, and extract slice object
bounds—slice objects have attributes start, stop, and step, any of which can be None
if omitted:
'''
class Indexer3:
    def __getitem__(self, index):
        if isinstance(index, int):                              # Test usage mode
            print('indexing', index)
        else:
            print('slicing', index.start, index.stop, index.step)
        

def tester3():
    X = Indexer3()
    X[99]
    X[1:99:2]
    X[1:]


if __name__ == '__main__':
    tester3()



"""
If used, the __setitem__ index assignment method similarly intercepts both index and
slice assignments—in 3.X:
    class IndexSetter:
        def __setitem__(self, index, value): # Intercept index or slice assignment
            ...
            self.data[index] = value # Assign index or slice
            
In fact, __getitem__ may be called automatically in even more contexts than indexing
and slicing—it’s also an iteration fallback option, as we’ll see in a moment.
"""