"Pitfall: Adding multiple inheritance naively"
class A:                                                            # In Python 3.X
    def act(self): print('A')

class B:
    def act(self): print('B')

class C(A):
    def act(self):
        super().act()                                               # super applied to a single-inheritance tree


if __name__ == '__main__':
    c = C()
    c.act()


""" 
If such classes later grow to use more than one superclass, though, super can become
error-prone, and even unusable—it does not raise an exception for multiple inheritance
trees, but will naively pick just the leftmost superclass having the method being run
(technically, the first per the MRO), which may or may not be the one that you want:
""" 
class C(A, B):                                                      # Add a B mix-in class with the same method
    def act(self):
        super().act()                                               # Doesn't fail on multi-inher, but picks just one!


if __name__ == '__main__':
    c = C()
    c.act()


class C(B, A):
    def act(self):
        super().act()                                               # If B is listed first, A.act() is no longer run!


if __name__ == '__main__':
    c = C()
    c.act()


'''
this silently masks the fact that you should probably be selecting superclasses
explicitly in this case, super usage may obscure a common source of errors in Python
'''
class C(A, B):                                                      # Traditional form
    def act(self):                                                  # You probably need to be more explicit here
        A.act(self)                                                 # This form handles both single and multiple inher
        B.act(self)                                                 # And works the same in both Python 3.X and 2.X
