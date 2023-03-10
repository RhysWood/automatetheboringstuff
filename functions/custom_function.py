#example of a function with parameter.
def hello(name):
    print('hello ' + name)

    
hello('Rhys')

#assign a function to a variable
def plusOne(number):
    return number + 1 

newnumber = plusOne(5)
print(newnumber)

#scope example
def spam():
    global eggs
    eggs = 99
    return eggs

eggs = 42
print(spam())