X, Y, Z = 43, 44, 45
S = 'Spam'                                  # Must be strings to store in file
D = {'a': 1, 'b': 2}
L = [1, 2, 3]

F = open('datafile.txt', 'w')               # Create output text file
F.write(S + '\n')                           # Terminate lines with \n
F.write('%s,%s,%s\n' % (X, Y, Z))           # Convert numbers to strings
F.write(str(L) + '$' + str(D) + '\n')       # Convert and separate with $
F.close()


# # Raw string display
chars = open('datafile.txt').read()
print(chars)


# Conversions
F = open('datafile.txt')                    # Open again
line = F.readline()                         # Read one line
print(line)

print(line.rstrip())                        # Remove end-of-line


line = F.readline()                         # Next line from file
print(line)

parts = line.split(',')                     # Split (parse) on commas
print(parts)

print(int(parts[1]))                        # Convert from string to int
# Convert all in list at once
numbers = [int(P) for P in parts]
print(numbers)


'''to convert the stored list and dictionary
     run them through eval'''
line = F.readline()
print(line)

parts = line.split('$')                     # Split (parse) on $
print(parts)

print(eval(parts[0]))                       # Convert to any object type

# Do same for all in list
objects = [eval(P) for P in parts]
print(objects)
