"Classes Can Intercept Python Operators"
'''
operator overloading lets objects coded with
classes intercept and respond to operations that work on built-in types: addition, slicing,
printing, qualification, and so on.

It’s mostly just an automatic dispatch mechanism
—expressions and other built-in operations route control to implementations in
classes.

Although we could implement all class behavior as method functions, operator overloading
lets objects be more tightly integrated with Python’s object model.

Moreover, because operator overloading makes our own objects act like built-ins, it tends to foster
object interfaces that are more consistent and easier to learn, and it allows class-based
objects to be processed by code written to expect a built-in type’s interface.
'''
