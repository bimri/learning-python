"Multiple Context Managers in 3.1, 2.7, and Later"
'''
the with statement may also specify multiple (sometimes
referred to as “nested”) context managers with new comma syntax
'''
with open('data') as fin, open('res', 'w') as fout:
    for line in fin:
        if 'some key' in line:
            fout.write(line) 
        

'''
the following uses with to open two files at once and zip together their lines, 
without having to manually close when finished
'''
with open('script1.py') as f1, open('script2.py') as f2:
    for pair in zip(f1, f2): 
        print(pair) 


"coding structure to do a line-by-line comparison of two text files"
with open('script1.py') as f1, open('script2.py') as f2:
    for (linenum, (line1, line2)) in enumerate(zip(f1, f2)): 
        if line1 != line2:
            print('%s\n%r\n%r' % (linenum, line1, line2)) 


'''
the preceding technique isn’t all that useful in CPython, because input file objects
don’t require a buffer flush, and file objects are closed automatically when reclaimed
if still open. In CPython, the files would be reclaimed immediately if the parallel scan
were coded the following simpler way:'''
for pair in zip(open('script1.py'), open('script2.py')):            # same effect, auto close 
    print(pair) 


""" 
In both cases, we can instead simply open files in individual statements and close after
processing if needed, and in some scripts we probably should—there’s no point in using
statements that catch an exception if it means your program is out of business anyhow!
""" 
fin  = open('script2.py') 
fout = open('upper.py', 'w') 
for line in fin:                                                    # Same effect as preceding code, auto close 
    fout.write(line.upper()) 


""" 
However, in cases where programs must continue after exceptions, the with forms also
implicitly catch exceptions, and thereby also avoid a try/finally in cases where close
is required. The equivalent without with is more explicit, but requires noticeably more
code: 
""" 
fin  = open('script2.py') 
fout = open('upper.py', 'w')
try:
    for line in fin:                                                # same effect but explicit close on error 
        fout.write(line.upper()) 
finally:
    fin.close() 
    fout.close() 


'''
On the other hand, the try/finally is a single tool that applies to all finalization cases,
whereas the with adds a second tool that can be more concise, but applies to only certain
objects types, and doubles the required knowledge base of programmers.
'''
