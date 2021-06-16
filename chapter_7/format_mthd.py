print('{}'.format(bin((2 ** 16) - 1)))
print('%s' % bin((2 ** 16) - 1)[2:])                        # Slice off 0b to get exact equivalent


# key and attribute references
print('{name} {job} {name}'.format(name='Bob', job='dev'))
print('%(name)s %(job)s %(name)s' % dict(name='Bob', job='dev'))

# common practice
D = dict(name='Bob', job='dev')
print('{0[name]} {0[job]} {0[name]}'.format(D))                    # Method, key references
print('{name} {job} {name}'.format(**D))                           # Method, dict-to-args
print('%(name)s %(job)s %(name)s' % D)                             # Expression, key references         


# Explicit value references
print('The {0} side {1} {2}'.format('bright', 'of', 'life'))            # Python 3.X, 2.6+
print('The {} side {} {}'.format('bright', 'of', 'life'))               # Python 3.1+, 2.7+
print('The %s side %s %s' % ('bright', 'of', 'life'))                   # All Pythons


# a single value can be given by itself, 
# but multiple values must be enclosed in a tuple
print('%s' % 1.23)                                      # Single value, by itself
print('%s' % (1.23,))                                   # Single value, in a tuple
print('%s' % ((1.23,),))                                # Single value that is a tuple


'''The formatting method, on the other hand, tightens 
this up by accepting only general function arguments'''
print('{0:.2f}'.format(1.2345))                         # Single value
print('{0:.2f} {1}'.format(1.2345, 99))                 # Multiple values
print('{0}'.format(1.23))                               # Single value, by itself
print('{0}'.format((1.23,)))                            # Single value that is a tuple
