"Records Revisited: Classes Versus Dictionaries"
'''
dictionaries, tuples, and lists to record properties
of entities in our programs, generically called records. It turns out that classes can often
serve better in this role—they package information like dictionaries, but can also bundle
processing logic in the form of methods.
'''
rec = ('Bob', 40.5, ['dev', 'mgr'])                         # Tuple-based record
print(rec[0])

rec = {}
rec['name'] = 'Bob'                                         # Dictionary-based record
rec['age'] = 40.5                                           # Or {...}, dict(n=v), etc.
rec['jobs'] = ['dev', 'mgr']

print(rec['name'])

'''
This code has substantially less syntax than the dictionary equivalent. It uses an empty
class statement to generate an empty namespace object. Once we make the empty
class, we fill it out by assigning class attributes over time, as before.

This works, but a new class statement will be required for each distinct record we will
need. We can instead generate instances of an empty class to
represent each distinct entity:
'''
class rec: pass

rec.name = 'Bob'                                            # Class-based record
rec.age  = 40.5
rec.jobs = ['dev', 'mgr']

print(rec.name)


class rec: pass

# make two records from the same class.
"Instances start out life empty, just like classes. We then fill in the records by assigning to attributes."
'there are two separate objects, and hence two separate name attributes'
pers1 = rec()                                               # Instance-based records
pers1.name = 'Bob'
pers1.jobs = ['dev', 'mgr']
pers1.age = 40.5

pers2 = rec()
pers2.name = 'Sue'
pers2.jobs = ['dev', 'cto']

print(pers1.name, pers2.name)


'''
Finally, we might instead code a more full-blown class to implement the record and its
processing—something that data-oriented dictionaries do not directly support:
'''
class Person:
    def __init__(self, name, jobs, age=None):                   # class = data = logic
        self.name = name 
        self.jobs = jobs 
        self.age  = age 
    
    def info(self):
        return (self.name, self.jobs)
    

rec1 = Person('Bob', ['dev', 'mgr'], 40.5)                  # Construction calls
rec2 = Person('Sue', ['dev', 'cto'])

print(rec1.jobs, rec2.info())                               # Attributes + methods


'''
This scheme also makes multiple instances, but the class is not empty this time: we’ve
added logic (methods) to initialize instances at construction time and collect attributes
into a tuple on request. The constructor imposes some consistency on instances here
by always setting the name, job, and age attributes, even though the latter can be omitted
when an object is made. Together, the class’s methods and instance attributes create a
package, which combines both data and logic.
'''


"""
To be fair to other tools, in this form, the two class construction calls above more closely
resemble dictionaries made all at once, but still seem less cluttered and provide extra
processing methods. In fact, the class’s construction calls more closely resemble Chapter
9’s named tuples—which makes sense, given that named tuples really are classes
with extra logic to map attributes to tuple offsets:

    >>> rec = dict(name='Bob', age=40.5, jobs=['dev', 'mgr'])                       # Dictionaries
    >>> rec = {'name': 'Bob', 'age': 40.5, 'jobs': ['dev', 'mgr']}
    >>> rec = Rec('Bob', 40.5, ['dev', 'mgr'])                                      # Named tuples
"""
