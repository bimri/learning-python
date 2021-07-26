"Unified try Statement Syntax"
''' 
When combined like this, the try statement must have either an except or a finally,
and the order of its parts must be like this:
    try -> except -> else -> finally

where the else and finally are optional, and there may be zero or more excepts, but
there must be at least one except if an else appears. Really, the try 
'''

# # Format 1
# try:                            
#     statements 
# except [type [as value]]:       # [type [,value]] in Python 2.X
#     statements
# [except [type [as value]]:
#     statements]* 
# [else:
#     statements]
# [finally:
#     statements]


# # Format 2
# try:                            
#     statements
# finally:
#     statements 



'''
Because of these rules, the else can appear only if there is at least one except, and it’s
always possible to mix except and finally, regardless of whether an else appears or
not. It’s also possible to mix finally and else, but only if an except appears too (though
the except can omit an exception name to catch everything and run a raise statement,
described later, to reraise the current exception). If you violate any of these ordering
rules, Python will raise a syntax error exception before your code runs.
'''
