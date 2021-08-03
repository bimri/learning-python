"String Type Conversions"
'''
3.X draws a much sharper distinction
—str and bytes type objects never mix automatically in expressions and never are
converted to one another automatically when passed to functions. A function that expects
an argument to be a str object won’t generally accept a bytes, and vice versa.

Because of this, Python 3.X basically requires that you commit to one type or the other,
or perform manual, explicit conversions when needed:
    • str.encode() and bytes(S, encoding) translate a string to its raw bytes form and
    create an encoded bytes from a decoded str in the process.
    • bytes.decode() and str(B, encoding) translate raw bytes into its string form and
    create a decoded str from an encoded bytes in the process.
'''
# encode & decode methods use either a default encoding for your platform
# or explicitly passed-in encoding name

S = 'bimri'
print(S.encode())                               # str->bytes: encode text into raw bytes
print(bytes(S, encoding='ascii'))               # str->bytes, alternative

B = b'codes'
print(B.decode())                               # bytes->str: decode raw bytes into text
print(str(B, encoding='latin-1'))               # bytes->str, alternative
print()

""" 
Two cautions here. First of all, your platform’s default encoding is available in the
sys module, but the encoding argument to bytes is not optional, even though it is in
str.encode (and bytes.decode).

Second, although calls to str do not require the encoding argument like bytes does,
leaving it off in str calls does not mean that it defaults—instead, a str call without an
encoding returns the bytes object’s print string, not its str converted form (this is usually
not what you’ll want!). Assuming B and S are still as in the prior listing:
"""
import sys 
print(sys.platform)                     # Underlying platform 
print(sys.getdefaultencoding())         # DEFAULT encoding for str here

"TypeError: string argument without an encoing"
# bytes(S)

print(str(B))                           # str without encoding
                                        # A print string, not conversion!
print(len(str(B)))
print(len(str(B, encoding='ascii')))    # Use encoding to convert to str


"When in doubt, pass in an encoding name argument in 3.X, even if it may have a default"
