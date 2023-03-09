name = ''
# while name != 'your name':
#   print('Please type your name')
#   name = input()
# print('Thank you')

# while True:
#   print('Please type your name')
#   name = input()
#   if name == 'your name':
#     break

spam = 0

while spam < 5:
  spam = spam + 1
  if spam == 3:
    continue
  print('spam is ' + str(spam)) 
  
#break will exit the loop
#continue will skip the current iteration and continue with the next iteration 