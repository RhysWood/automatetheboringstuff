#most things you can do with lists you can also do with strings
#indexing, for loops, slicing etc
name = 'Rhys'
print(name[1:3])
#returns hy
print('Rhy' in name)
#returns True

for letter in name:
    print(letter)
    
#returns
#R
#H
#Y
#S

#a list value is a mutable data type, it can have values added, removed or changed
#a string is an immutable data type, it cannot be changed

#you have to create a new sting to mutate it, eg

cat_name = 'Winston a cat'
new_name = cat_name[0:7] + ' the ' + cat_name[10:13]
print(new_name)
#returns winston the cat

#The difference between immutable and mutable comes up with 'references'
#When you assign a list to a variable you are actually assigning a list reference to a variable

spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello!'
print(cheese)
#returns [0, 'Hello!', 2, 3, 4, 5]
print(spam)
#spam has also been changed! 
#returns [0, 'Hello!', 2, 3, 4, 5]

#a list is referncing an ID in memory, so when you change it you change anything which refers to that reference
#this is the same for all mutable data


#THIS IS HOW IT CAN CREATE BUGS
def eggs(some_parameter):
    some_parameter.append('hello')

bacon = [1, 2, 3] 
eggs(bacon)
print(bacon)
#returns [1, 2, 3, 'hello']

#so the change made inside a loca scope of eggs is changing the globally scoped bacon list


#if you want a completely seperate list - there is a module called copy 
import copy
cheese = ['A', 'B', 'C', 'D']
wine = copy.deepcopy(cheese)
#creates a copy with a new reference number, so completely seperate


#Line Continuation - you can get python to ignore indentation, it does it for lists automatically
friends = ['Luke',
           'James'
           'JJ',
           'Rob']

#you can also use backslash
print('I want this to start' + \
       ' a new line')
