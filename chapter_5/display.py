num = 1 / 3.0

# Print explicitly
print(num)

# String formatting expresssion
print('%e' % num)

# Alternative floating-point format
print('%4.2f' % num)

#String formatting method
print('{0:4.2f}'.format(num))


# repr & str use cases on Interractive prompt
# >>> repr('spam')                # used by echoes: as-code form
# >>> str('spam')                 # used by print: user-friendly form
