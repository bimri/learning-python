# sys.stdout is just a normal file object
import sys

x, y, z = 'spam', 12, [12, 23, 45]
temp = sys.stdout                                           # Save for restoring later

sys.stdout = open('log1.txt', 'a')                          # Redirect prints to a file
print('spam')                                               # Prints go to file, not here
print(1, 2, 3)                                              
sys.stdout.close()                                          # Flush output to disk
sys.stdout = temp                                           # Restore original stream

print('back here')                                          # Prints show up here again
print(open('log1.txt').read())                              # Result of earlier prints
print()
print('ENTER FILE KEYWORD TO SAVE THE HUSTLE FROM ABOVE')


# FILE KEYWORD
log = open('log2.txt', 'a')
print(x, y, z, file=log)                                   # Print to a file-like object
print('==> Orginal output not disturbed')


'''Redirects forms of print are handy if you need to 
   print to both files and the standard output stream
   in the same program'''
log = open('log3.txt', 'w')
print(1, 3, 3, 4, file=log)
print(345, 78, 678, file=log)
log.close()
print(7, 8, 9)

# read outputs that were printed earlier to log3.txt file
print(open('log3.txt').read())



# PRINTING ERROR MESSAGES to the standart error stream
import sys
sys.stderr.write(('Bad!' * 8) + '\n')

print('Bad!' * 5, file=sys.stderr)
