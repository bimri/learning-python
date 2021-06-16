'''
The Python for loop begins with a header line that specifies an assignment target (or
targets), along with the object you want to step through. The header is followed by a
block of (normally indented) statements that you want to repeat:

            for target in object:                                                                   # Assign object items to target
                statements                                                                          # Repeated loop body: use target
            else:                                                                                   # Optional else part
                statements                                                                          # If we didn't hit a 'break'


            for target in object:                                                                   # Assign object items to target
                statements
                if test: break                                                                      # Exit loop now, skip else
                if test: continue                                                                   # Go to top of loop now
            else:
                statements                                                                          # If we didn't hit a 'break'
'''

# Examples: - basic usage
for x in ["spam", "eggs", "ham"]:
    print(x, end=' ')
print()

sum = 0 
for x in [1, 2, 3, 4]:
    sum = sum + x

print(sum)


prod  = 1
for item in [1, 2, 3, 4]: prod *= item
print(prod)


# Other data types
S = "lumberjack"
T = ("and", "I'm", "okay")

for x in S: print(x, end=' ')                               # iterate over a string
print()

for x in T: print(x, end=' ')                               # iterate over a tuple
print()
