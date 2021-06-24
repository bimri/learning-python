from firstClass import FirstClass


class SecondClass(FirstClass):                              # Inherits setdata
    """
    SecondClass defines the display method to print with a different format. By defining
    an attribute with the same name as an attribute in FirstClass, SecondClass effectively
    replaces the display attribute in its superclass.
    """
    def display(self):
        """
        Recall that inheritance searches proceed upward from instances to subclasses to superclasses,
        stopping at the first appearance of the attribute name that it finds. In this
        case, since the display name in SecondClass will be found before the one in First
        Class, we say that SecondClass overrides FirstClass’s display. Sometimes we call this
        act of replacing attributes by redefining them lower in the tree overloading.
        """
        print('Current value = "%s"' % self.data)


# Make an instance that inherists the setdata method in FirstClass verbatim
'''
>>> z = SecondClass()
>>> z.setdata(42)                                           # Finds setdata in FirstClass
>>> z.display()                                             # Finds overridden method in SecondClass
Current value = "42"
'''
