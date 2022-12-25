def user_details(**kwargs):
    # print(kwargs)
    for i in kwargs:
        print(i, 'is', kwargs[i])
user_details(age=24, name= 'Anu', gender='female') #keyword argument 
user_details(age=20, name= 'Appu', gender='male', place="calicut") #prints in dictionary