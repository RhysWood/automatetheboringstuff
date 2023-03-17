#finding an index
spam = ['hello', 'hi', 'howdy', 'heyas']
print(spam.index('hi'))

#to add new values to a list, use append() and insert() methods
spam.append('moose')
print(spam)

#insert is similat but it can insert anywhere in said list
spam.insert(1, 'chicken')
print(spam)

#append and insert only work on list data type!

#there is also a remove method
spam.remove('hi')
print(spam)

#sort method - very handy! 
list_of_numbers = [2, 6, -7, 3.14, 14]
list_of_numbers.sort()
print(list_of_numbers)

#can also do this with strings, sorts to alphabetical order
list_of_words = ['dogs', 'badgers', 'ants', 'elephants', 'cats']
list_of_words.sort()
print(list_of_words)

#you can also pass keyword arg to sort - reverse
list_of_words.sort(reverse=True)
print(list_of_words)

#you cannot sort a list with different data types
#it uses ascii-betical so any uppercase characters come first
#if you want true alpabetical sorting you can use this
spam.sort(key=str.lower)