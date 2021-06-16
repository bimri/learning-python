f = open('test.txt', 'r')                                   # read contents into a string
print(f.read())


# read by characters
f = open('test.txt')                                        
while True:
    char = f.read(1)                                        # read by character
    if not char: break                                      # empty string means end-of-file
    print(char)

for char in open('test.txt').read():
    print(char)


'''processes each character, but it loads 
the file  into memory all at once'''
f = open('test.txt')
while True:
    line = f.readline()                                     # read line by line
    if not line: break 
    print(line.rstrip())                                    # line alread has a \n


# You typically read binary data in blocks
f = open('test.txt', 'rb')
while True:
    chunk = f.read(10)                                      # Read byte chunks: up to 10 bytes
    if not chunk: break
    print(chunk)


# read text files line by line
for line in open('test.txt').readlines():
    print(line.rstrip())

# file iterators to automatically read 
# one line on each loop iteration
for line in open('test.txt'):                               # use iterators: best for text input
    print(line.rstrip())


# reverse a file’s lines
for line in reversed(open('test.txt').readlines()): ...
