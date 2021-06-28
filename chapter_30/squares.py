class Squares:
    def __init__(self, start, stop):                        # Save state when create
        self.value = start - 1
        self.stop  = stop 
    def __iter__(self):                                     # Get iterator on iter
        return self
    def __next__(self):                                     # Return a square on each iteration
        if self.value == self.stop:                         # Also called by next built-in
            raise StopIteration
        self.value += 1
        return self.value ** 2 

    
def tester():
    for i in Squares(1, 5):                                 # for calls iter which calls __iter__
        print(i, end=' ')                                   # Each iteration calls __next__
    

if __name__ == "__main__":
    tester()
