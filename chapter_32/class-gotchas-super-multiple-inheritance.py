"Multiple Inheritance: Order Matters"
# Python always searches superclasses from left to right, according to their order in the header line.

# class ListTree:
#     def __str__(self): ... 

# class Super:
#     def __str__(self): ...

# class Sub(ListTree, Super):                                             # Get ListTree's __str__ by listing it first
#     x = Sub()                                                           # Inheritance searches ListTree before Super 


""" 
But now suppose Super and ListTree have their own versions of other same-named
attributes, too. If we want one name from Super and another from ListTree, the order
in which we list them in the class header won’t help—we will have to override inheritance
by manually assigning to the attribute name in the Sub class:
""" 
# class ListTree:
#     def __str__(self): ...
#     def other(self): ...

# class Super:
#     def __str__(self): ...
#     def other(self): ...

# class Sub(ListTree, Super):                                             # Get ListTree's __str__ by listing it first
#     other = Super.other                                                 # But explicitly pick Super's version of other
#     def __init__(self):
#         ...

# x = Sub()                                                               # Inheritance searches Sub before ListTree/Super


""" 
Here, the assignment to other within the Sub class creates Sub.other—a reference back
to the Super.other object. Because it is lower in the tree, Sub.other effectively hides
ListTree.other, the attribute that the inheritance search would normally find. Similarly,
if we listed Super first in the class header to pick up its other, we would need to
select ListTree’s method explicitly:
""" 

# class Sub(Super, ListTree):                                             # Get Super's other by order
#     __str__ = Lister.__str__                                            # Explicitly pick Lister.__str__


"Scopes in Methods and Classes"
def generate():
    class Spam:                                                         # Spam is a name in generate's local scope
        count = 1
        def method(self):
            print(Spam.count)                                           # Visible in generate's scope, per LEGB rule (E)
    return Spam()

generate().method()


def generate():
    return Spam() 

class Spam():                                                           # Define at top level of module 
    count = 1                                                           
    def method(self):
        print(Spam.count)                                               # Visible in module, per LEGB rule (E)
    
generate().method()



def generate(label):                                                    # Returns a class instead of instance
    class Spam:                                                         # Define in module scope 
        count = 1 
        def method(self):
            print("%s=%s" % (label, Spam.count)) 
    return Spam


if __name__ == "__main__":
    aClass = generate("Gotchas")          # Generate a class
    I = aClass()                          # Create an instance of the class
    I.method()                            # Call the method
