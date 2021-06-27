# update Person object on database
"prints the database and gives a raise to one of our stored objects each time"
import shelve
db = shelve.open('persondb')                                # Reopen shelve with same filename

for key in sorted(db):                                      # Iterate to display database objects
    print(key, '\t=>', db[key])                             # Prints with custom format

jenny = db['Jenny Writes']                                   # Index by key to fetch
jenny.giveRaise(.10)                                        # Update in memory using class's method
db['Jenny Writes'] = jenny                                   # Assign to key to update in shelve
db.close()                                                  # Close after making changes
