"Mixing String Types"
# Must pass expected types to function and method calls

B = b'spam'
# B.replace('pa', 'XY')                     # TypeError: expected an object with the buffer interface
print(
    B.replace(b'pa', b'XY')
)

B = B'spam'
# B.replace(bytes('pa'), bytes('xy'))       # TypeError: string argument without an encoding
print(
    B.replace(bytes('pa', 'ascii'), bytes('xy', 'utf-8'))
)


# Must convert manually in 3.X mixed-type expressions

# b'ab' + 'cd'                          # TypeError: can't concat bytes to str
print(  
    b'ab'.decode() + 'cd'
)                                       # bytes to str

print(
    b'ab' + 'cd'.encode()
)                                       # str to bytes

print(
    b'ab' + bytes('cd', 'ascii')
)                                       # str to bytes


'''
Although you can create bytes objects yourself to represent packed binary data, they
can also be made automatically by reading files opened in binary mode.
'''
