#Lists look like a js array, like this
list = ['dog', 'cat', 'python']
print(list[0]) #returns single index
#you can have lists within lists
spam = [['dog', 'cat', 'python'], [10, 20, 30, 40, 50]]
print(spam[1][0])
#you can use minus numbers to grab data from the end of the list
animals = ['elephant', 'bat', 'tiger', 'hippo']
print('The ' + animals[-1] + ' is afraid of the ' + animals[-2])

#you can also slice - the below starts at index 1 and goes up to but doesn't include index 3
print(animals[1:3]) #returns a new list 

#we can assign new values to a list, replacing old ones
animals[1] = 'hello'
print(animals)

#we can slice in sections like so
animals[1:3] = ['frog', 'fish', 'octopus']
print(animals)

#and if we leave out one of the opperators, it will assume it is from the begginning or until the end.
animals[1:] = ['frog', 'fish', 'octopus']
print(animals)
animals[:4] = ['frog', 'fish', 'octopus']
print(animals)

#del statement deletes item from list
del animals[0]
print(animals)

#len returns the number of items in a list
print(len(animals))

#we can concatonate lists
print([1,2,3,4] + [5,6,7,8])

#in and not in operators
greetings = ['waddup', 'hey', 'hello', 'hi', 'bonjour']
print('waddup' in greetings)
print('waddup' not in greetings)