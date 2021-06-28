class SkipObject:
    def __init__(self, wrapper):                        # Save item to be used
        self.wrapped = wrapper 
    def __iter__(self):
        return SkipIterator(self.wrapped)               # New iterator each time

class SkipIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped                          # Iterator state information
        self.offset  = 0 
    def __next__(self):
        if self.offset >= len(self.wrapped):            # Terminate iterations
            raise StopIteration 
        else:
            item = self.wrapped[self.offset]            # else return and skip 
            self.offset += 2 
            return item 


if __name__ == '__main__':
    alpha = 'abcdefg'
    skipper = SkipObject(alpha)                         # Make container object
    I = iter(skipper)
    print(next(I), next(I), next(I))                    # Visit offset 0, 2, 4

    for x in skipper:                                   # for calls __iter__ automatically 
        for y in skipper:                               # Nested fors call __iter__ again each time
            print(x + y, end=' ')                       # Each iterator has its own state, offset
    
    print()
    # Classes versus slices
    S = 'wxyzdhk'
    for x in S[::2]:
        for y in S[::2]:                                # New object on each iteration
            print(x + y, end=' ')

    print()        
    """
    This isn’t quite the same, though, for two reasons. First, each slice expression here will
    physically store the result list all at once in memory; iterables, on the other hand, produce
    just one value at a time, which can save substantial space for large result lists.
    Second, slices produce new objects, so we’re not really iterating over the same object in
    multiple places here. To be closer to the class, we would need to make a single object
    to step across by slicing ahead of time:


    This is more similar to our class-based solution, but it still stores the slice result in
    memory all at once (there is no generator form of built-in slicing today), and it’s only
    equivalent for this particular case of skipping every other item.
    """

    S = 'uioplkj'
    S = S[::2]
    print(S)
    for x in S:
        for y in S:                                     # Same object, new iterators
            print(x + y, end=' ')
    

    
"""
Each active loop has its own position in the string because
each obtains an independent iterator object that records its own state information:

Here, there is just one SkipObject iterable, with multiple iterator objects created from it.
"""
