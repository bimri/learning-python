"Metaclass Methods Versus Class Methods"
'''
Though they differ in inheritance visibility, much like class methods, metaclass methods
are designed to manage class-level data. In fact, their roles can overlap—much as
metaclasses do in general with class decorators—but metaclass methods are not accessible
except through the class, and do not require an explicit classmethod class-level
data declaration in order to be bound with the class. In other words, metaclass methods
can be thought of as implicit class methods, with limited visibility:
'''
class A(type):
    def a(cls):                                             # Metaclass method: gets class
        cls.x = cls.y + cls.z


class B(metaclass=A):
    y, z = 11, 22
    @classmethod                                            # Class method: gets class
    def b(cls):
        return cls.x


B.a()                               # Call metaclass method; visible to class only
B.x                                 # Creates class data on B, accessible to normal instances

I = B()
I.x, I.y, I.z

I.b()                               # Class method: sends class, not instance; visible to instance
# I.a()                             # Metaclass methods: accessible through class only; AttributeError
