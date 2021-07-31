"with/as Context Managers"
'''
Python 2.6 and 3.0 introduced a new exception-related statement—the with, and its
optional as clause. This statement is designed to work with context manager objects,
which support a new method-based protocol, similar in spirit to the way that iteration
tools work with methods of the iteration protocol.
'''

""" 
In short, the with/as statement is designed to be an alternative to a common try/
finally usage idiom; like that statement, with is in large part intended for specifying
termination-time or “cleanup” activities that must run regardless of whether an exception
occurs during a processing step.
""" 

'''
Unlike try/finally, the with statement is based upon an object protocol for specifying
actions to be run around a block of code. This makes with less general, qualifies it as
redundant in termination roles, and requires coding classes for objects that do not
support its protocol. On the other hand, with also handles entry actions, can reduce
code size, and allows code contexts to be managed with full OOP.
'''

"Basic Usage"
# with expression [as variable]:              # with an optional part in square
#     with-block 

""" 
The expression here is assumed to return an object that supports the context management
protocol. This object may also return a value that will be assigned to the name variable 
if the optional as clause is present.

Note that the variable is not necessarily assigned the result of the expression; the result
of the expression is the object that supports the context protocol, and the variable may
be assigned something else intended to be used inside the statement. The object returned
by the expression may then run startup code before the with-block is started,
as well as termination code after the block is done, regardless of whether the block
raised an exception or not.

Some built-in Python objects have been augmented to support the context management
protocol, and so can be used with the with statement.
"""

with open(r'E:\E:\practice\relative_path') as myfile:
    """ 
    this object also supports the context management protocol used by the
    with statement. After this with statement has run, the context management machinery
    guarantees that the file object referenced by myfile is automatically closed, even if the
    for loop raised an exception while processing the file.
    """ 
    for line in myfile:
        print(line)
        ... # more code here ...


# try/finally statement
myfile = open(r'E:\E:\practice\relative_path')
try:
    for line in myfile:
        print(line)
        ... # more code here ... 
finally:
    myfile.close() 


# Python’s multithreading
'''
Here, the context management machinery guarantees that the lock is automatically
acquired before the block is executed and released once the block is complete, regardless
of exception outcomes.
'''
import threading

lock = threading.lock()     
with lock:
    # critical section of code 
    ... # access shared resources ...


# Decimal module context management
'''
the decimal module also uses context managers to simplify
saving and restoring the current decimal context, which specifies the precision and
rounding characteristics for calculations:

After this statement runs, the current thread’s context manager state is automatically
restored to what it was before the statement began. To do the same with a try/
finally, we would need to save the context before and restore it manually after the
nested block.
'''
import decimal 

with decimal.localcontext() as ctx:
    ctx.prec = 2 
    x = decimal.Decimal('1.00') / decimal.Decimal('3.00')
