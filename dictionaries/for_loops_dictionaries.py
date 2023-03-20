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