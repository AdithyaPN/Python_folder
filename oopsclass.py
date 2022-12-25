class AcerNitro5: #class
    keyboard = 'qwerty' #properties as variables
    dispaly = 'LED'
    processor = '8GB RAM'
    manufacturer = 'Acer'
    price = 55000
    color = 'Black'

    def power_on(self): #self must
        print('ON')    

    def play_music(self):
        print('music')

#Object creation
lap1 = AcerNitro5() # now allocate to memory. creates 2 copies of this classs
lap2 = AcerNitro5()
lap1.play_music()
lap1.color = 'metallic grey'
