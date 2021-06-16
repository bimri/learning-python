# Python detects block boundaries automatically
# by line indentation

x = 1
if x:
    y = 2
    if y:
        print('Block 2')
    print('Block 1')
print('Block0')


x = 'SPAM'
if 'rubbery' in 'shrubbery':
    print(x * 8)                            # Prints 8 "SPAM"
    x += 'NI'
    if x.endswith('NI'):
        print(x)                            # Prints "SPAMNISPAMNI"

