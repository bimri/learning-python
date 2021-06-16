# User-defined  docstrings
"""
Module documentation
Words Go Here
"""

spam = 40

def square(x):
    '''
    function documentation
    can we have your liver then?
    '''
    return x ** 2                                           # square


class Employee:
    "class documentation"
    pass


print(square(4))
print(square.__doc__)


# >>> import docstrings
# 16
# function documentation
# can we have your liver then?
# >>> print(docstrings.__doc__)
# Module documentation
# Words Go Here
# >>> print(docstrings.square.__doc__)
# function documentation
# can we have your liver then?
# >>> print(docstrings.Employee.__doc__)
# class documentation