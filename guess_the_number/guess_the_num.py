import random

print('Hey there! What is your name?')
name = input()
secretNumber = random.randint(1, 20)
print('Well ' + name + ' I am thinking of a number between 1 and 20. Try and guess!')

for guessesTaken in range(1, 7):
    print('Take a guess')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low!')
    elif guess > secretNumber:
        print('Your guess is too high!')
    else:
        break
    
if guess == secretNumber:
    print('You got it ' + name + '!')
    print('It took you ' + str(guessesTaken) + ' tries.')
else:
    print('Nope - the number I was thinking of was ' + str(secretNumber), ' better luck next time!')