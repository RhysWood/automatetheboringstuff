def div42by(divideby):
    try:
        return 42 / divideby
    except ZeroDivisionError:
        print('You tried to divide by zero')
        
print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))

print('How many cats do you own?')
numOfCats = input()
try:
    if int(numOfCats) < 0: 
        print('You cannot have a minus number of cats!')
    elif int(numOfCats) >= 4:
        print('wow, that is a lot of cats!')
    else:
        print('That is not that many cats')
except ValueError:
    print('you need to type a number')