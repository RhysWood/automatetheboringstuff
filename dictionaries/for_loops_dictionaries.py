eggs = {
    'name': 'Winston',
    'species': 'cat',
    'age': 12
}
spam = {
    'species': 'cat',
    'name': 'Winston',
    'age': 12
}

for k in eggs.keys():
    print(k)
#returns 
# name
# species
# age

for v in eggs.values():
    print(v)
#returns 
# Winston
# cat
# 12

#you can use multiple assignment trick with items()

for k, v in eggs.items():
    print(k, v)
    
#name Winston
#species cat
#age 12

#otherwise touples would be assigned to a single variable

for i in eggs.items():
    print(i)
#('name', 'Winston')
#('species', 'cat')
#('age', 12)

print('cat' in eggs.values())
#True

#rather than checking with an if statement everytime like this:
if 'color' in eggs:
    print(eggs['color'])

#python gives us a get method which takes two values(what is it searching for, and a fallback method), used like this: 
eggs.get('age', 0)
#returns 12
eggs.get('color', '')
#returns ''
picnicItems = {
    'apples': 5,
    'cups': 2
}
print('I am bringing ' + str(picnicItems.get('napkins', 0)) + ' napkins to the picnic')
#I am bringing 0 napkins to the picnic

