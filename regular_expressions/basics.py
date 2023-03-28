import re

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

# \d is a special character in regular expressions that stands for a digit character
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#mo is match object
mo = phoneNumRegex.search(message)
print(mo.group())

#find all phone numbers in a string with findall()
print(phoneNumRegex.findall(message))
