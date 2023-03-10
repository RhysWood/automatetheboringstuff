import random

# print(random.randint(1, 10))

def randomNumGame():
    randnum = random.randint(1, 10)
    guess = input()
    print(guess)



print(randomNumGame())