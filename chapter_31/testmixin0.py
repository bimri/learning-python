"Listing instance attributes with __dict__"

from listinstance import ListInstance            # Get lister tool class                      # Get lister tool class

class Super:
    def __init__(self):                                     # Superclass __init__
        self.data1 = 'spam'                                 # Create instance attrs
    def ham(self):
        pass 


class Sub(Super, ListInstance):                             # Mix in ham and a __str__
    def __init__(self):
        Super.__init__(self)                                
        self.data2 = 'eggs'                                 # More instance attrs
        self.data3 = 24
    def spam(self):                                         # Define another method here
        pass 


if __name__ == "__main__":
    X = Sub()
    print(X)                        # Run mixed-in __str__



'''
This is where multiple inheritance comes in handy: by
adding ListInstance to the list of superclasses in a class header (i.e., mixing it in), you
get its __str__ “for free” while still inheriting from the existing superclass(es).
'''
