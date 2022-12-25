def display(n1,n2):
    print('First function')
    sum = n1 + n2 #local variable
    sub = n1 - n2
    return sum,sub
# result = display(1,7) #function call
# print(result) #we can use index number to get each single operations
# print('sum is ', result[0])
result1,result2 = display(5,2)
print('sum is ' + str(result1))
print('difference is ' + str(result2))

