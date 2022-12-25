# a = 10
# b = 0
# result = 0
# try:
#     result = a / b
# except: #only works when try has any problem
#     print('Undefined')
# print(result)

# file = open('text.txt', 'w') # w means write
# file.write('insersion \n')

# file = open('text2.txt', 'a') # a means append
# file.append('append') # file not found exception
try:
    file = open('text2.txt', 'r') # r means wright
    print(file.read())
except FileNotFoundError as e: #built in error function
    print(e)
else:
    print('No error found')
finally:
    file.close()

