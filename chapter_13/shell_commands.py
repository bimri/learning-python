import os 

F = os.popen('dir')                 # read line by line
print(
    F.readline()
)
print()

F = os.popen('dir')                 # read by sized blocks
print(
    F.read(50)
)
print()

print(
    os.popen('dir').readlines()[0]      # read all lines: index
)
print()

print(
    os.popen('dir').read()[:50]         # read all at once: slice
)
print()

# File line iterator loop
for line in os.popen('dir'):
    print(line.rstrip())
print()
print()

'''shell command’s output in a simple console window'''
# print(
#     os.system('systeminfo')
# )

for line in os.popen('systeminfo'): print(line.rstrip())
print()
print()

# Formatted, limited display
for (i, line) in enumerate(os.popen('systeminfo')):
    if i == 4: break
    print('%05d) %s' % (i, line.rstrip()))
print()
print()

# Parse for specific lines, case neutral
for line in os.popen('systeminfo'):
    parts = line.split(':')
    if parts and parts[0].lower() == 'system type':
        print(parts[1].strip())
