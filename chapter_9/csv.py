import csv

rdr = csv.reader(open('csvdata.txt'))

for row in rdr: print(row)
# ['a', 'bbb', 'cc', 'dddd']
# ['11', '22', '33', '44']