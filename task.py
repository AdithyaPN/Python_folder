# def correct_answer():
#     pass

# def total_mark():
#     pass

# def online_exam():
#     while True:
#         print('\nOnline Examination')
#         print('1.Python')
#         print('2.PHP')
#         print('3.Flutter')
#         choice = int(input('Enter your choice: '))

#     if choice == 1:
#         print('\n Welcome to Python Examination')
#         print('\n1: Who first developed python?')
#         print('a.Guido Van Russom')
#         print('b.Dennis Ritchie')
#         print('c.James Gosling')
#         answer1 = input('Enter your answer: ')

#         if answer1 == 'a':
#             print('Correct')
#             correct_answer()
#             total_mark()
#         else:
#             print('Wrong answer')

#     elif choice == 2:
#         print('\n Welcome to Php Examination')
#         print('\n1: Who first developed Php?')
#         print('a.Guido Van Russom')
#         print('b.Dennis Ritchie')
#         print('c.Rasmus Lerdorf ')
#         answer1 = input('Enter your answer: ')

#         if answer1 == 'c':
#             print('Correct')
#             correct_answer()
#             total_mark()
#         else:
#             print('Wrong answer')

#     elif choice == 3:
#         print('\n Welcome to Flutter Examination')
#         print('\n1: Who first developed Flutter?')
#         print('a.Guido Van Russom')
#         print('b.Navneet Dalal and Mehul Nariyawala')
#         print('c.Rasmus Lerdorf ')
#         answer1 = input('Enter your answer: ')

#         if answer1 == 'b':
#             print('Correct')
#             correct_answer()
#             total_mark()
#         else:
#             print('Wrong answer')

#     else:
#         print('\nInvalid choice. Select a valied choice:')
#         online_exam()

class BankAccount:

    def __init__(self,ac_h_name,ac_num,ifsc,brnch,mob,email,atm):
        self.acc_holder_name = ac_h_name
        self.acc_number = ac_num
        self.ifsc_code = ifsc
        self.branch = brnch
        self.mobile_number = mob
        self.email_id = email    
        self.atm_pin = atm

    def display_details(self):
        print(self.acc_holder_name)
        print(self.acc_number)
        print(self.ifsc_code)
        print(self.branch)
        print(self.mobile_number)
        print(self.email_id)
        print(self.atm_pin)

account1 = BankAccount('Adithya',4435363535,'ifsc001','Vadakara',7510701619, 'adi@gmail.com',8880)
account2 = BankAccount('Anu',4435363578,'ifsc001','Vadakara',8090701619, 'anu@gmail.com',8890)
account1.display_details()
account2.display_details()

    