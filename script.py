# name = input('What is your name?\n')
# print('Hi, %s.' % name)

# This program says hello  and asks for my name
print('Hello there! What is your name?')
myName = input()
print('nice to meet you, ' + myName)
print('the length of your name is: ')
print(len(myName))
print('How old are you?')
myAge = input()
#cannot concatonate a number, hence str()
print('you will be ' + str(int(myAge) + 1) + ' in a year.')
