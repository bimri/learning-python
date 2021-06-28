"3.X’s __index__ Is Not Indexing!"
'''
this method returns an integer value for an instance
when needed and is used by built-ins that convert to digit strings (and in retrospect,
might have been better named __asindex__):
'''

class C:
    def __index__(self):
        return 255 
    

def tester():
    X = C()
    print(hex(X))              # Integer value
    print(bin(X))
    print(oct(X))


if __name__ == '__main__':
    tester()



"""
Although this method does not intercept instance indexing like __getitem__, it is also
used in contexts that require an integer—including indexing:
"""
def tester():
    X = C()
    print(('C' * 256)[255])
    print(('C' * 256)[X])                   # As index (not X[i])
    print(('C' * 256)[X:])                  # As index (not X[i:])


if __name__ == '__main__':
    tester()