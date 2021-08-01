"Functions Can Signal Conditions with raise"
'''
User-defined exceptions can also signal nonerror conditions. For instance, a search
routine can be coded to raise an exception when a match is found instead of returning
a status flag for the caller to interpret.
'''
class Found(Exception): pass 

# def searcher():
#     if ... success... :
#         raise Found()                           # Raise exceptions instead of returning flags 
#     else:
#         return 
    
# try:
#     searcher() 
# except Found:                                   # Exception if item was found
#     ...success...
# else:                                           # else returned: not found 
#     ...failure...


""" 
More generally, such a coding structure may also be useful for any function that cannot
return a sentinel value to designate success or failure. In a widely applicable function,
for instance, if all objects are potentially valid return values, it’s impossible for any
return value to signal a failure condition. Exceptions provide a way to signal results
without a return value:
"""
# class Failure(Exception): pass

# def searcher():
#     if ...success...:
#         return ...founditem...
#     else:
#         raise Failure()

# try:
#     item = searcher()
# except Failure:
#     ...not found...
# else:
#     ...use item here...

'''
Because Python is dynamically typed and polymorphic to the core, exceptions, rather
than sentinel return values, are the generally preferred way to signal such conditions.
'''