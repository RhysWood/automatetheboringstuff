#how to get around 's in strings

#use double quotes
print("this is a string with 's in it")

#escape characters
print('this is a string with \'s in it')

#new line
print('this is a string \n with a new line')
print('Hello there!\nHow are you?\nI\'m doing fine.')

#to stop python doing this, use a raw string using r
print(r'this is a string \n with a new line')

#you can also use """ triple quotes to make a string, it will print out as it is
print("""this is a string
      this is a new line
      thanks
      Rhys""")

#triple quotes are useful for massive sections of text or documenation

#strings work like lists, you can index them and slice them etc
spam = 'Hello World!'
print(spam[0])
#H
print(spam[1:5])
#ello
print(spam[-1])
#! (last character)
print('Hello' in spam)
#True
#case sentitive
print('hello' in spam)
#False