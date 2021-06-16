'''File objects are Python code’s main interface 
   to external files on your computer'''

# Opening & Writing to a file store to your CWD
f = open('data.txt', 'w')                               # Make a new file in output mode('w' is write)
print(f.write('Hello bimri, here we meet again\n'))     # Write string of characters to it
print(f.write('This time round - let nothing pass you by with files\n'))

f.close()


# Reading contents of your file
f = open('data.txt')
text = f.read()
print(text)
print(text.split())


# Best way to read a file is to not read it at all
# Files provide an iterator that automatically reads
# line by line in for loops and other contexts.
for line in open('data.txt'): print(line)

