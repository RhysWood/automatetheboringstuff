def sumOfNumbers(number):
    finishedlist=[]
    answer = 0
    for i in range(1, number+1):
        finishedlist.append(i)
    for x in finishedlist:
        answer = answer + x;
    return answer
    
print(sumOfNumbers(10))

#refactored
def sum_of_numbers(number):
    finished_list = list(range(1, number+1))
    answer = sum(finished_list)
    return answer

print(sum_of_numbers(10))

