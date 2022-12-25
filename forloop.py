# for i in range(0,10): #it prints 0 to 9 only
#     print(i)

# for i in range(1,11): #it prints 1 to 10 
#     print(i)

# for i in range(11,-1,-1): #it prints 10 to 0 only, third -1 is for indicate reverse
#     print(i)

# for i in range(0,10,2): #increments by 2
#     print(i)

# name = 'Adithya'
# for i in name:
#     print(i)

# to print list items
# name = ['Anu', 'Adhi', 'Vishnu']
# for i in name:
#     print(i)

#nested for syntax 
# for i in range(1,11):
#     for j in range(10,1,-1):
#         print(j)
#     print(i)

# for i in range(1,10):
#     if i == 6:
#         break
#     print(i)

# for i in range(1,10):# skip 6
#     if i == 6:
#         continue
#     print(i)
for i in range(3,11):
    if i==5:
        pass # we can't let a condition statementless, so we use "pass" or "none" keyword
    else:
        print(i)
   