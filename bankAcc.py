class BankAccount:

    def __init__(self,ac_h_name,ac_num,ifsc,brnch,mob,email,atm):
        self.acc_holder_name = ac_h_name
        self.__acc_number = ac_num
        self.__ifsc_code = ifsc
        self.__branch = brnch
        self.mobile_number = mob
        self.email_id = email    
        self.__atm_pin = atm

    # def display_details(self):
    #     print(self.acc_holder_name)
    #     print(self.acc_number)
    #     print(self.ifsc_code)
    #     print(self.branch)
    #     print(self.mobile_number)
    #     print(self.email_id)
    #     print(self.atm_pin)

    #get method to access the variable
    def getAccountNumber(self):
        return self.__acc_number

    def getAtmPin(self):
        return self.__atm_pin

    #set method to update value
    def setAtmPin(self, new_pin): #new_pin is the new variable
        #atm pin validation
        if len(str(new_pin)) == 4 and  type(new_pin) == int:
            self.__atm_pin = new_pin
        else:
            print('Invalid pin')
account1 = BankAccount('Adithya',4095363535,'ifsc001','Vadakara',7510701619, 'adi@gmail.com',8880)
print(account1.getAccountNumber())
print(account1.getAtmPin())
account1.setAtmPin(1919)
print(account1.getAtmPin())

    