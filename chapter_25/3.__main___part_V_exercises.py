def countLines(name):
    file = open(name)
    return len(file.readlines())

def countChars(name):
    return len(open(name).read())

def test(name):                                             # Or pass file object
    return countLines(name), countChars(name)               # Or return a dictionary


if __name__ == '__main__':
    print(test('mymod.py'))


'''
% python mymod.py
(13, 346)
'''


# command-line arguments; user input to provide the filename to be counted
if __name__ == '__main__':
    print(test(input('Enter file name:')))                  # Console(raw_input in 2.X)

if __name__ == '__main__':
    import sys                                              # Command line
    print(test(sys.argv[1]))
