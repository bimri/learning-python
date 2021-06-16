table = {'1975': 'Holy Grail', 
        '1979': 'Life of Brian',
        '1983': 'The Meaning of Life'}

year = '1983'
movie = table[year]                         # dict[key] => Value
print(movie)


for year in table:
    print('\n' + year + '\t' + table[year] + '\n')


# Mapping values to keys
table = {'Holy Grail': '1975',      
         'Life of Brian': '1979',
         'The Meaning of Life': '1983'}

print(table['Holy Grail'])
print(list(table.items()))

print([title for (title, year) in table.items() if year == '1975'])

# map values back to keys
K = 'Holy Grail'
print(table[K])                                                 # Key=>Value(normal usage)

V = '1975'
print([key for (key, value) in table.items() if value == V])    # Value=> Key
print([key for key in table.keys() if table[key] == V])         # Ditto
