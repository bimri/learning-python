import sys

print('{1:10} = {1:10}'.format('spam', 123.3456))
print('{0:>10} = {1:<10}'.format('spam', 123.3456))
print('{0.platform} = {1[kind]:<10}'.format(sys, dict(kind='laptop')))

print('{:10} = {:10}'.format('spam', 123.4567))
print('{:>10} = {:<10}'.format('spam', 123.4567))
print('{.platform:>10} = {[kind]:<10}'.format(sys, dict(kind='laptop')))


'''Floating-point numbers support the same type codes 
    and formatting specificity in formatting method calls 
            as in % expressions.'''
print('{0:e}, {1:.3e}, {2:g}'.format(3.14159, 3.14159, 3.14159))
print('{0:f}, {1:.2f}, {2:06.2f}'.format(3.14159, 3.14159, 3.14159))


'''Hex, octal, and binary formats are supported by the 
            format method as well'''
print('{0:X}, {1:o}, {2:b}'.format(255, 255, 255))                  # Hex, octal, binary
print(bin(255), int('11111111', 2), 0b11111111)                     # Other to/from binary
print(hex(255), int('FF', 16), 0xFF)                                # Other to/from hex
print(oct(255), int('377', 8), 0o377)                               # Other to/from octal, in 3.X


'''Formatting parameters can either be hardcoded in format strings or taken from the
arguments list dynamically by nested format syntax'''
print('{0:.2f}'.format(1 / 3.0))                            # Parameters hardcoded
print('%.2f' % (1 / 3.0))                                   # Ditto for expression
print('{0:.{1}f}'.format(1 / 3.0, 4))                       # Take value from arguments
print('%.*f' % (4, 1 / 3.0))                                # Ditto for expression


# building data ahead of time in both
data = dict(platform=sys.platform, kind='laptop')
print('My {kind:<8} runs {platform:>8}'.format(**data))
print('My %(kind)-8s runs %(platform)8s' % data)


print('{:,d}'.format(999999999999))
print('{:,d} {:,d}'.format(9999999, 8888888))
print('{:,.2f}'.format(296999.2567))
