"General Form"
'''
class is a compound statement, with a body of statements typically indented appearing
under the header. In the header, superclasses are listed in parentheses after the class
name, separated by commas. Listing more than one superclass leads to multiple inheritance
'''

"""
class name(superclass,...):             # Assign to name
    attr = value                        # Shared class data
    def method(self,...):               # Methods
        self.attr = value               # Per-instance data
"""

'''
Within the class statement, any assignments generate class attributes, and specially
named methods overload operators; for instance, a function called __init__ is called
at instance object construction time, if defined.
'''