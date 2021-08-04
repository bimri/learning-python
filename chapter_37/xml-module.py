"XML Parsing Tools"
'''
XML is a tag-based language for defining structured information, commonly used to
define documents and data shipped over the Web. Although some information can be
extracted from XML text with basic string methods or the re pattern module, XML’s
nesting of constructs and arbitrary attribute text tend to make full parsing more accurate.

Because XML is such a pervasive format, Python itself comes with an entire package of
XML parsing tools that support the SAX and DOM parsing models, as well as a package
known as ElementTree—a Python-specific API for parsing and constructing XML. Beyond
basic parsing, the open source domain provides support for additional XML tools,
such as XPath, Xquery, XSLT, and more.
'''

"""
There are at least four basic ways to accomplish this (not counting more advanced tools
like XPath). First, we could run basic pattern matching on the file’s text, though this
tends to be inaccurate if the text is unpredictable. Where applicable, the re module we
met earlier does the job—its match method looks for a match at the start of a string,
search scans ahead for a match, and the findall method used here locates all places
where the pattern matches in the string (the result comes back as a list of matched
substrings corresponding to parenthesized pattern groups, or tuples of such for multiple
groups):
"""

# File patternparse.py

import re
text  = open(r'E:\practice\learning_python\chapter_37\mybooks.xml').read()
found = re.findall('<title>(.*)</title>', text)
for title in found: print(title)
print()


"""
Second, to be more robust, we could perform complete XML parsing with the standard
library’s DOM parsing support. DOM parses XML text into a tree of objects and provides
an interface for navigating the tree to extract tag attributes and values; the interface
is a formal specification, independent of Python:
"""
# File domparse.py

from xml.dom.minidom import parse, Node
xmltree = parse(r'E:\practice\learning_python\chapter_37\mybooks.xml')
for node1 in xmltree.getElementsByTagName('title'):
    for node2 in node1.childNodes:
        if node2.nodeType == Node.TEXT_NODE:            
            print(node2.data)


"""
As a third option, Python’s standard library supports SAX parsing for XML. Under the
SAX model, a class’s methods receive callbacks as a parse progresses and use state
information to keep track of where they are in the document and collect its data:
"""
# File saxparse.py

import xml.sax.handler
class BookHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.inTitle = False
    def startElement(self, name, attrs):
        if name == 'title':
            self.inTitle = True
    def characters(self, content):
        if self.inTitle:
            print(content)
    def endElement(self, name):
        if name == 'title':
            self.inTitle = False

# import xml.sax
# parser = xml.sax.make_parser()
# handler = BookHandler() 
# parser.setContentHandler(handler)
# parser.parse(r'E:\practice\learning_python\chapter_37\mybooks.xml')

"""
Finally, the ElementTree system available in the etree package of the standard library
can often achieve the same effects as XML DOM parsers, but with remarkably less code.
It’s a Python-specific way to both parse and generate XML text; after a parse, its API
gives access to components of the document:
"""
# File etreeparse.py

# from xml.etree.ElementTree import parse
# tree = parse('mybooks.xml')
# for E in tree.findall('title'):
#     print(E.text)
