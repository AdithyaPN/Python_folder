class Employee:

    def __init__(self):
        print('init Employee')

    def check_in(self):
        print('checked in')

    def check_in(self):
        print('checked out')
empObj = Employee()

class Accouts(Employee):

    def __init__(self):
        print('init accounts')
    
    def billing(self):
        print('print bills')

    def customer_details(self):
        print('customer details')

accObj = Accouts()

class Marketing(Employee):

    def __init__(self):
        print('init Marketing')

markObj = Marketing()






