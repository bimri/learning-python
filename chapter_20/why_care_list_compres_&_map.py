open('myfile').readlines()

[line.rstrip() for line in open('myfile').readlines()]
[line.rstrip() for line in open('myfile')]
list(map((lambda line: line.rstrip()), open('myfile')))


"SQL database API returns query results as a sequence of sequences"
listoftuple = [('bob', 35, 'mgr'), ('sue', 40, 'dev')]

# pick up all the values from a selected column (manually)
[age for (name, age, job) in listoftuple]
list(map((lambda row: row[1]), listoftuple))

'The first of these makes use of tuple assignment to unpack row tuples in the list, and the second uses indexing.'
