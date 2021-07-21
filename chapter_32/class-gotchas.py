"Class Gotchas"
# Most class issues can be boiled down to namespace issues

'Changing Class Attributes Can Have Side Effects'
""" 
As with builtin
lists and dictionaries, you can change them in place by assigning to their attributes
—and as with lists and dictionaries, this means that changing a class or instance object
may impact multiple references to it. 

Because all instances generated from a class share the class’s namespace, any changes at
the class level are reflected in all instances, unless they have their own versions of the
changed class attributes.
""" 

if __name__ == "__main__":
    class X:
        a = 1                   # Class attribute
    
    I = X()                     # Make a class instance
    print(I.a)                  # Inherited by instance
    print(X.a)

    X.a = 2                     # May change more than X
    print(I.a)                  # I changes too

    J = X()                     # J inherits from X's runtime values
    print(J.a)                  # (but assigning to J.a changes a in J, not X or I)


    """ 
    you can actually get work done by changing class attributes without ever making
    a single instance—a technique that can simulate the use of “records” or “structs” in
    other languages.
    """
    class X: pass                               # Make a few attribute namespaces
    class Y: pass

    X.a = 1                                     # Use class attributes as variables
    X.b = 2                                     # No instances anywhere to be found
    X.c = 3
    Y.a = X.a + X.b + X.c
    
    print()
    for X.i in range(Y.a): print(X.i)           # Prints 0..5


    """ 
    Here, the classes X and Y work like “fileless” modules—namespaces for storing variables
    we don’t want to clash.
    """
    class Record: pass
    X = Record()
    X.name = 'bob'
    X.job = 'Pizza maker'

    Y = Record()
    Y.name = 'sue'
    Y.job = 'Bartender'
    Y.age = 40
    print(Y.name, 'is', Y.job, 'and is', Y.age, 'years old')
