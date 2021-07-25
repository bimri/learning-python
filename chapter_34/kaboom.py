"Example: Catching Built-in Exceptions"
'''
Sometimes, though, you’ll want to catch errors and recover from them instead. If you
don’t want your program terminated when Python raises an exception, simply catch it
by wrapping the program logic in a try. This is an important capability for programs
such as network servers, which must keep running persistently.
'''

def kaboom(x, y):
    print(x + y)                    # Trigger TypeError


try:
    kaboom([0, 1, 2], 'spam') 
except TypeError:                   # Catch and recover here
    print('Hello world!')
print('resuming here')              # Continue here if exception or not 


""" 
Since an exception is “dead” after it’s been
caught like this, the program continues executing below the try rather than being terminated
by Python. 
""" 


'''
Keep in mind that once you’ve caught an error, control resumes at the place where you
caught it (i.e., after the try); there is no direct way to go back to the place where the
exception occurred (here, in the function kaboom). In a sense, this makes exceptions
more like simple jumps than function calls—there is no way to return to the code that
triggered the error.
'''
