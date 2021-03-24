import random

class TryHitTheNumber:
    def __init__(self):
        self.random_value = 0
        self.minimum_value = 1
        self.maximum_value = 100
        self.try_again = True
        
    def start(self):
        self.GenerateRandomNumber()
        self.RequestRandomValue()
        try:
            while self.try_again == True:
                if int(self.answer) > self.random_value:
                    print ('Hit a lower number!')
                    self.RequestRandomValue()
                elif int(self.answer) < self.random_value:
                    print ('Hit a higher number!')
                    self.RequestRandomValue()
                if int(self.answer) == self.random_value:
                    self.try_again = False
                    print ('CONGRATULATIONS! YOU HITTED THE NUMBER!')
        except:
            print ('Please, only answer with numbers!')
            self.start()

    def RequestRandomValue(self):
        self.answer = input('Hit a number between 1-100: ')

    def GenerateRandomNumber(self):
        self.random_value = random.randint(self.minimum_value, self.maximum_value)
        
hitnumber = TryHitTheNumber()
hitnumber.start()