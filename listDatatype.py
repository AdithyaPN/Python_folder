#lists
mark = [43, 40, 46, 'Adhi']
print(mark[2]) # index value
print(len(mark)) # length of the list

mark[1]=39 # to update the value in list
print(mark)

print(mark[1:3])# to get the sublist
print(mark[1:]) #end not defined
print(mark[:3]) #starting not defined

#joining to lists
student = ['Anu', 'Ammu', 'Amal']
print(mark + student)

print(mark*3) #repeat the same values in a list


#tuple:
num = ( 2,3,3,4,5,5,'Athira') #values inside a function bracket,can't update the elements in a tuple
# num[1]=39
# print(num) can't update single element

tuple1 = ('python', 7, 5, 7)
tuple2 = (( 8.0, 8, 6, 'Anu'), 6, 4, 'Karthika')
print(tuple2[0][1]) #will get 8 from the first tuple element (8.0,8,6.'Anu')