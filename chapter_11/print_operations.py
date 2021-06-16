'''
printing converts one or more objects to their textual representations, adds
some minor formatting, and sends the resulting text to either standard output or another
file-like stream

print is strongly bound up with the notions of files and streams in Python
'''

# calls to the 3.X function have the following form print
'''
print([object, ...][, sep=' '][, end='\n'][, file=sys.stdout][, flush=False])
'''

print()                                         # Display a blank line

x = 'spam'
y = 99
z = ['eggs']

print(x, y, z)                                  # Print three objects per defaults

'''print calls add a space between the objects printed'''
# To suppress this, sens an empty string to "sep" keyword
print(x, y, z, sep='')                          # Suppress separator

# Suppress line break
print(x, y, z, end='')

# Two prints, same output line
print(x, y, z, end=''); print(x, y, z)

# Custom line end
print(x, y, z, end='...\n')


# Multiple keywords
print(x, y, z, sep='...', end='!\n')

# Order doesn't matter
print(z, x, y, end='!\n', sep='___')


# Print to a file
print(z, y, x, sep='...', file=open('data.txt', 'w'))
# Back to stdout
print(x, y, z)

# Display file text
print(open('data.txt').read())


'''If you need to display more specific formatting'''
text = '%s: %-4.f, %05d' % ('Result', 3.14159, 42)
print(text)

print('%s: %-4f, %05d' % ('Result', 3.14159, 42))


# Print Stream Redirection
import sys                                          # Printing the hard way
print(sys.stdout.write('hello world\n'))


# Manual stream redirection
import sys
sys.stdout = open('log.txt', 'a')                   # Redirects prints to a file
                                                    # append mode
                                                    
print(x, y, x)                                      # shows up in log.text
