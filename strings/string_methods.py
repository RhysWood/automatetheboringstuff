#string methods return a new string rather than modifying the original string, strings are immutable
spam = 'Hello world!'
print(spam.upper())
#HELLO WORLD!
#to change the original string, you need to reassign it
spam = spam.upper()
print(spam)
#HELLO WORLD!
#you can also use spam = spam.lower() or spam = spam.title()
spam = spam.title()
print(spam)
#Hello World!

#islower() and isupper() return a boolean value
eggs = 'hello world!'
print(eggs.islower())
#True
print(eggs.isupper())
#False

#other boolean string methods
#isalpha() returns True if the string consists only of letters and is not blank
#isalnum() returns True if the string consists only of letters and numbers and is not blank
#isdecimal() returns True if the string consists only of numeric characters and is not blank
#isspace() returns True if the string consists only of spaces, tabs, and newlines and is not blank
#istitle() returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters

print('Hello world!'.startswith('Hello'))
print('Hello world!'.startswith('H'))
#True

print('Hello world!'.endswith('world!'))
#True

#Join method
','.join(['cats', 'rats', 'bats'])
#cats,rats,bats

#split method
print('My name is Rhys'.split())
#['My', 'name', 'is', 'Rhys']
print('My name is Rhys'.split('m'))
#['My na', 'e is Rhys']

#ljust() and rjust() methods return a padded version of the string with spaces inserted to justify the text
print('Hello'.rjust(10))
#     Hello
print('Hello'.ljust(10))
#Hello
print('Hello'.rjust(20, '*'))
#***************Hello
print('Hello'.center(20, '-'))
#-------Hello--------

#strip method removes whitespace from the beginning and end of a string
hey = 'Hello'.rjust(20)
print(hey.strip())
#Hello

#replace method replaces all instances of the first string with the second string
hello = 'Hello there!'
print(hello.replace('e', 'XYZ'))
#HXYZllo thXYZrXYZ!