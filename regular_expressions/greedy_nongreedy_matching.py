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


batRegex4 = re.compile(r'Bat(wo)+man')
#The + matches one or more. The group that precedes the + must appear at least once.
#It is not optional.
mo2 = batRegex4.search('The Adventures of Batman')
print(mo2 == None) #True
print(mo2 is None) #True

#using the backslash to escape the special characters
regex5 = re.compile(r'\+\*\?')
print(regex5.search('I learned about +*? regex syntax'))
#<re.Match object; span=(16, 19), match='+*?'>

#question mark is used to match zero or one of the group preceding it.
#star matches zero or more.
#plus matches one or more.


haRegex = re.compile(r'(Ha){3}')
print(haRegex.search('He said "HaHaHa"'))
#<re.Match object; span=(9, 15), match='HaHaHa'>

#may or may not have a comma seperating the three phone number groups.
phoneRegex1 = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
print(phoneRegex1.search('My numbers are 415-555-1234,555-4242,212-555-0000'))
#<re.Match object; span=(15, 49), match='415-555-1234,555-4242,212-555-0000'>


#maybe you want a range of repetitions. between 3 and 5.
haRegex1 = re.compile(r'(Ha){3,5}')
print(haRegex.search('He said "HaHaHaha"'))
#<re.Match object; span=(9, 15), match='HaHaHa'>

#any numeric digit between, 3 and 5 of them
digitRegex = re.compile(r'(\d){3,5}')
print(digitRegex.search('1234567890'))
#<re.Match object; span=(0, 5), match='12345'>
#it matches the first 5 digits, 12345. not 123456. It is a greedy match

#see below to do a non-greedy match
digitRegex1 = re.compile(r'(\d){3,5}?')
print(digitRegex1.search('1234567890'))
#<re.Match object; span=(0, 3), match='123'>