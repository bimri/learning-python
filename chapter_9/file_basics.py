# Opening Files
myfile = open('data.txt', 'w')
myfile.write('Coming online\n')
myfile.write('Hello text world\n')
myfile.write('Goodbye text world\n')
myfile.close()                                  # Flush output buffers to disk


myfile = open('data.txt')                       # Open for text input: 'r' is default
print(myfile.readline())                        # Read the lines back
print(myfile.readline())
print(myfile.readline())
print(myfile.readline())                        # Empty string: end-of-file


# Read all at once into string
print(open('data.txt').read())                  # User-friendly display


# Use file iterators, not reads
for line in open('data.txt'):
    print(line, end='')


for line in open(r'C:\Users\avatar\Desktop\code\relative path.txt'):
    print(line, end='')
