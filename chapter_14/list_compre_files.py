f = open('script2.py')
lines = f.readlines()
print(lines)

# sanitize
lines = [line.rstrip() for line in lines]
print(lines)


# we don’t even have to open the file ahead of time
lines = [line.rstrip() for line in open('script2.py')]
print(lines)


# list comprehension equivalent to the file iterator uppercase
print(
    [line.upper() for line in open('script2.py')]
)

print(
    [line.rstrip().upper() for line in open('script2.py')]
)

print(
    [line.split() for line in open('script2.py')]
)

print(
    [line.replace(' ', '|') for line in open('script2.py')]
)

print(
    [('sys' in line, line[:5]) for line in open('script2.py')]
)