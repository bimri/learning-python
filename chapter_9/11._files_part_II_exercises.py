F = open('myfile.txt', 'w')
F.write('Hello file world!\n')
F.close()

fr = open('myfile.txt')                                 # 'r' is default open mode
print(fr.read())
