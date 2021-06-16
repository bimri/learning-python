import re 

# Searches for substring with the word
# "Hello", followed by zero or more tabs or spaces,
# followed by arbitrary characters to be saved as 
# a matched group, terminated by the word "world".
match = re.match('Hello[ \t]*(.*)world', 'Hello     Python world')
print(match.group(1))

# Picks out three groups separated by slashes
match1 = re.match('[/:](.*)[/:](.*)[/:](.*)', '/usr/home:lumberjack')
print(match1.groups())
