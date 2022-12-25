class Laptop:
    

    def __init__(self,clr,syz,ram,batry,wght,prssr,mnf,modl,priz):
        self.color = clr #instance variable declaration
        self.size = syz
        self.ram = ram
        self.battery = batry
        self.weight = wght
        self.processor = prssr
        self.manufacturer = mnf
        self.model = modl
        self.price = priz

    def power_on(self):
        print('power on')

    def power_off(self):
        print('power off')

    def display_details(self):
        print(self.color)
        print(self.size)
        print(self.ram)
        print(self.battery)
        print(self.weight)
        print(self.processor)
        print(self.manufacturer)
        print(self.model)
        print(self.price)

acer = Laptop('metallic black', 15,8,5000,600,1,'acer','Nitro 5',55000)
# acer.manufacturer = 'acer'
# acer.model = 'acer Nitro 5'
# acer.price = 55000

hp = Laptop('silver', 15,8,5000,600,1,'hp','pavillion',65000)
# hp.manufacturer = 'hp'
# hp.model = 'pavllion'
# hp.price = 65000

hp.display_details() #object calling
acer.display_details()