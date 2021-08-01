"Exception Design Tips and Gotchas"
'Catching Too Little: Use Class-Based Categories'
'''
On the other hand, neither should handlers be too specific. When you list specific
exceptions in a try, you catch only what you actually list. This isn’t necessarily a bad
thing, but if a system evolves to raise other exceptions in the future, you may need to
go back and add them to exception lists elsewhere in your code.
'''

try:
    ...
except (MyExcept1, MyExcept2):                      # Breaks if you add a MyExcept3 later
    ...                                             # Nonerrors
else:
    ...                                             # Assumed to be an error


""" 
Careful use of the class-based exceptions can make
this code maintenance trap go away completely. If you catch a general
superclass, you can add and raise more specific subclasses in the future without having
to extend except clause lists manually—the superclass becomes an extendible exceptions
category:
"""

try:
    ...
except SuccessCategoryName:                         # OK if you add a MyExcept3 subclass later
    ...                                             # Nonerrors
else:
    ...                                             # Assumed to be an error


""" 
In other words, a little design goes a long way. The moral of the story is to be careful
to be neither too general nor too specific in exception handlers, and to pick the granularity
of your try statement wrappings wisely. Especially in larger systems, exception
policies should be a part of the overall design.
"""
