'''
Common Python expression statements:
        spam(eggs, ham)                     Function calls
        spam.ham(eggs)                      Method calls
        spam                                Printing variables in the interactive interpreter
        print(a, b, c, sep='')              Printing operations in Python 3.X
        yield x ** 2                        Yielding expression statements
'''

x = print('spam')                           # print is a function call expression in 3.X
print(x)                                    # But it is coded as an expression statement



'''Expression Statements and In-Place Changes'''
L = [1, 2]
L.append(3)                                 # Append is an in-place change
print(L)

# Mistake - newcomers
L = L.append(4)                             # But append returns None, not L
print(L)                                    # So we lose our list!


# KEY POINT: -
'''call in-place change operations without as
                signing their results'''
                