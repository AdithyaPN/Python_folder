# i = 22
# def display():
#     # i = 10 # it is considered as a new local variable
#     global i # this helps to update
#     i = 10
#     print('Inside function ', i)
# display()
# print('Outside function ', i)

#User details
def user_details(name, age, gender):
    print('Name is : ', name)
    print('Age is : ', age)
    print('Gender is : ', gender)
user_details('Adhi', 24, 'female')
# user_details(22, 'Geethu', 'female')
user_details(age=24,name= 'Anu', gender='female') #keyword argument 