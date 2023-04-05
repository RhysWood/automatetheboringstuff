import re

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
mo.group()
# 'Batmobile'
mo = batRegex.search('Batmotorcycle lost a wheel')
# mo = None

#Groups are created in regular expressions with parentheses
#The first group is group 1, the second group is group 2, and so on.
#The | character is called a pipe. You can use it anywhere you want to match one of many expressions.
#The (Batman|Tina Fey) part of the regular expression is called a group.
#When a regular expression has groups, the findall() method returns a list of tuples.