print('my name is')

#while example
i=0
while i < 5:
    print('jimmmy five times ' + str(i))
    i = i + 1
    
#range example
for i in range(12, 16): #up to but not including 16
    print(i)

for i in range(0, 10, 2): #up to but not including 10, increment by 2 (step arg)
    print(i)


#Gauss example
solution = 0
for i in range(101):
    solution = solution + i
    
print(solution)       