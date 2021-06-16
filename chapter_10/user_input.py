while True:
    reply = input('Enter text:')
    if reply == 'stop': break
    print(reply.upper())


# Doing Math on User Inputs
while True:
    reply = input('Enter text for math on user:')
    if reply == 'stop': break
    print(int(reply) ** 2)
print('Bye')


# Handling Errors by Testing Inputs
S = '123'
T = 'xxx'
print(S.isdigit(), T.isdigit())

while True:
    reply = input('Enter text for handling errors segment:')
    if reply == 'stop':
        break 
    elif not reply.isdigit():
        print('Bad' * 8)
    else:
        print(int(reply) ** 2)
print('Bye')


# Handling Errors with try statements
while True:
    reply = input('Enter text for try statement:')
    if reply == 'stop': break
    try:
        num = int(reply)
    except:
        print('Bad!' * 8)
    else:
        print(num ** 2)
print('Bye')


# Supporting floating-point numbers
while True:
    reply = input('Enter text to show support for floating-point no.:')
    if reply == 'stop': break
    try:
        print(float(reply) ** 2)                
    except:
        print('Bad!' * 8)
print('Kwaheri')


# Nesting Code Three Levels Deep
while True:
    reply = input('Enter text for 3 levels deep:')
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print('Bad!' * 8)
    else:
        num = int(reply)
        if num < 20:
            print('low')
        else:
            print(num ** 2)
print("Tothi'e")
