S = 'Spam'

#Find method
print(S.find('pa'))     # find the offset of a string in S

print(S)

# Replace method
print(S.replace('pa', 'XYZ'))       # Replace occurences of a string in S with another
print(S)                            # Remains undefiled - immutable!


# Splitting method
line = 'aaa,bbb,ccccc,dd'
print(line.split(','))          # split on delimiter into a list of substrings


# Upper/Lowercase conversions
S = 'Spam'
print(S.upper())            # upper-and lowercase conversion
print(S.isalpha())          # Content tests: isaplpha, isdigit 


# Whitespace
line1 = 'aaa,bbb,ccccc,dd\n'
print(line1)
print(line1.rstrip())               # Remove whitespace chars on the right side
print(line1.rstrip().split(','))     # Combine two operations


# Formatting
print('%s, eggs, %s' % ('spam', 'SPAM!'))                   # Formatting expression(all)
print('{0}, eggs, and {1}'.format('spam', 'SPAM!'))         # Formatting METHOD
print('{}, eggs and {}'.format('spam', 'SPAM!'))            # Numbers are optional


# Numerical reports
print('{:,.2f}'.format(296999.2567))        # Separators, decimal digits
print('%.2f | %+05d' % (3.14159, -42))      # Digits, padding, signs
