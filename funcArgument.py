# def add(num1, num2=0):  #default argument
#     sum = num1 + num2
#     print(sum)
# add(2,2)     #required argument

def argument(*args):
    result = 0 
    for i in args: 
        result = result+i
    print(result)
argument(2,4)
argument(8,4,2)