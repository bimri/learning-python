"The Context Management Protocol"
'''
Here’s how the with statement actually works:
    1. The expression is evaluated, resulting in an object known as a context manager that
    must have __enter__ and __exit__ methods.
    
    2. The context manager’s __enter__ method is called. The value it returns is assigned
    to the variable in the as clause if present, or simply discarded otherwise.
    
    3. The code in the nested with block is executed.
    
    4. If the with block raises an exception, the __exit__(type, value, traceback) method
    is called with the exception details. These are the same three values returned by
    sys.exc_info, described in the Python manuals and later in this part of the book.
    If this method returns a false value, the exception is reraised; otherwise, the exception
    is terminated. The exception should normally be reraised so that it is
    propagated outside the with statement.
    
    5. If the with block does not raise an exception, the __exit__ method is still called,
    but its type, value, and traceback arguments are all passed in as None.
'''

class TraceBlock:
    def message(self, arg):
        print('running ' + arg) 
    
    def __enter__(self):
        print('starting with block')
        return self 
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is None:
            print('exited normally\n')
        else:
            print('raise an exception! ' + str(exc_type))
            return False        # Propagate


if __name__ == '__main__':
    with TraceBlock() as action:
        action.message('test 1') 
        print('reached') 
    
    with TraceBlock() as action:
        action.message('test 2')
        raise TypeError
        print('not reached')

"Context managers can also utilize OOP state information and inheritance"
