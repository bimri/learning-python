class Squares:                                  # Non __iter__ equivalent
    def __init__(self, start, stop):                    
        self.start = start
        self.stop  = stop 
    def gen(self):
        for value in range(self.start, self.stop + 1 ):
            yield value ** 2


if __name__ == '__main__':
    for i in Squares(1, 5).gen(): print(i, end=' ')

    print()
    S = Squares(1, 5)
    I = iter(S.gen())                            # Call generator manually for iterable/iterator
    print(next(I))



"""
Coding the generator as __iter__ instead cuts out the middleman in your code, though
both schemes ultimately wind up creating a new generator object for each iteration:
    • With __iter__, iteration triggers __iter__, which returns a new generator with
    __next__.

    • Without __iter__, your code calls to make a generator, which returns itself for
    __iter__.
"""
