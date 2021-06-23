'''
This module’s money function defaults to dollars, but supports other currency symbols
by allowing you to pass in non-ASCII Unicode characters. The Unicode ordinal with
hexadecimal value 00A3, for example, is the pound symbol, and 00A5 is the yen. You
can code these in a variety of forms, as:

    • The character’s decoded Unicode code point ordinal (integer) in a text string, with
    either Unicode or hex escapes (for 2.X compatibility, use a leading u in such string
    literals in Python 3.3)

    • The character’s raw encoded form in a byte string that is decoded before passed,
    with hex escapes (for 3.X compatibility, use a leading b in such string literals in
    Python 2.X)

    • The actual character itself in your program’s text, along with a source code encoding
    declaration
'''
from formats import money

X = 54321.987

print(money(X), money(X, 0, ''))
print(money(X, currency=u'\xA3'), money(X, currency=u'\u00A5'))
print(money(X, currency=b'\xA3'.decode('latin-1')))

print(money(X, currency=u'\u20AC'), money(X, 0, b'\xA4'.decode('iso-8859-15')))
print(money(X, currency=b'\xA4'.decode('latin-1')))
