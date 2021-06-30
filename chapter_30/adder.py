"Right-Side and In-Place Uses: __radd__ and __iadd__"
'''
for every binary expression, we can implement
a left, right, and in-place variant.

Though defaults are also applied if you don’t
code all three, your objects’ roles dictate how many variants you’ll need to code.
'''
class Adder:
    def __init__(self, value=0):
        self.data = value 
    
    def __add__(self, other):
        return self.data + other 
    

if __name__ == "__main__":
    x = Adder(5)
    print(x + 2)

    # Type error => 2 + x


"""To implement more general expressions, and hence support commutative-style operators,
code the __radd__ method as well. Python calls __radd__ only when the object on
the right side of the + is your class instance, but the object on the left is not an instance
of your class. The __add__ method for the object on the left is called instead in all other
cases

(all of this section’s five Commuter classes are coded in file commuter.py in the
book’s examples, along with a self-test):
"""