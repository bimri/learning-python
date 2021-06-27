class SharedData:
    """
    any type of name assignment at the top level of a class 
    statement creates a same-named attribute of the resulting 
    class object.
    """
    spam = 42                                                       # Generates a class data attribute

x = SharedData()                                                    # Make two instances
y = SharedData()
print(x.spam, y.spam)                                               # They inherit and share 'spam' (a.k.a. SharedData.spam)


# We can change it by going through the class name, 
# and we can refer to it through either instances or the class:
"Such class attributes can be used to manage information that spans all the instances"
SharedData.spam = 99
print(x.spam, y.spam, SharedData.spam)


'''
Assignments to instance attributes create or change the names in the instance, rather
than in the shared class. More generally, inheritance searches occur only on attribute
references, not on assignment: assigning to an object’s attribute always changes that
object, and no other.

For example, y.spam is looked up in the class by inheritance, but
the assignment to x.spam attaches a name to x itself.
'''
x.spam = 88
print(x.spam, y.spam, SharedData.spam)
