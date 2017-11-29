# -*- coding: utf-8 -*-

# imports argv from sys
from sys import argv

# "define" the file name
script, filename = argv

# opens the file
txt = open(filename)

# gives out text and filename
print "Here's your file %r:" % filename
# prints the content of the file
print txt.read()

# gives out the text
print "Type the filename again:"
# lets you type in the filename again
file_again = raw_input(">")

# opens the file
txt_again = open(file_again)
# prints the content of the file
print txt_again.read()
