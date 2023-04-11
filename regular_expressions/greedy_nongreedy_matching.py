import re

batRegex = re.compile(r'batman|batwoman')
#could also be done like this:
batRegex1 = re.compile(r'Bat(wo)?man')

mo = batRegex1.search('The Adventures of Batwoman')

if mo is not None:
    print(mo.group())
else:
    print("No match found")
#Batwoman
    
#The ? says that the group that precedes it is optional.
#the regex will match text that has zero instances or one instance of the group preceding the question mark.

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My number is 415-555-4242.')
print(mo.group())
#415-555-4242
matchObject = phoneRegex.search('My number is 555-4242.')
print(matchObject.group())
#555-4242



batRegex3 = re.compile(r'Bat(wo)*man')
# The * says that the group that precedes it can occur any number of times in the text, including zero times.
mo1 = batRegex3.search('The Adventures of Batwowowowowoman')
print(mo1.group())
#Batwowowowowoman
