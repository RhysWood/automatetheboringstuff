#for loops with lists

supplies = ['pens', 'staplers', 'binders', 'macbooks']
for i in range(len(supplies)):
    print('Index ' + str(i) + 'in supplies is: ' + supplies[i])
    
#multiple assignment trick with list
cat = ['fat', 'orange', 'loud']
size, color, disposition = cat
print(size)
print(color)
print(disposition)

#or 3 for three on assignment

size, color, disposition = 'skinny', 'black', 'quiet'
print(size)
print(color)
print(disposition)

#usually done for swapping variables
a = 'AAA'
b= 'BBB'
a, b = b, a 
print(a)