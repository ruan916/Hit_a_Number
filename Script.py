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
        while self.try_again == True:
            if (self.answer) > self.random_value:
                print ('Hit a higher number!')
                self.RequestRandomValue()
            elif (self.answer) < self.random_value:
                print ('Hit a lower number!')
                self.RequestRandomValue()
            self.try_again = False
            print ('CONGRATULATIONS! YOU HITTED THE NUMBER!')

    def RequestRandomValue(self):
        self.answer = int(input('Hit a number between 1-100: '))

    def GenerateRandomNumber(self):
        print(random.randint(self.minimum_value, self.maximum_value))
        
hitnumber = TryHitTheNumber()
hitnumber.start()