#dictionaries are like objects - with key value pairs
myCat = {
    'size': 'fat',
    'color': 'ginger',
    'disposition': 'loud'
}

print('My cat has ' + myCat['color'] + ' fur.')

#unlike lists, items in dictionaries are unordered
print([1, 2, 3] == [3, 2, 1])
#returns FALSE

#while this
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
print(eggs == spam)
#returns TRUE

#trying to a key when it is not in a dictionary returns a key error - eg spam[color]

#you can use in and not in with dictionaries
print('name' in eggs)
#returns True
print('name' not in eggs)
#returns False

#variables hold references to dictionary Values

print(list(eggs.keys()))
#['name', 'species', 'age']
print(list(eggs.values()))
#['Winston', 'cat', 12]
print(list(eggs.items()))
#[('name', 'Winston'), ('species', 'cat'), ('age', 12)]