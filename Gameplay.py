import random

class Gameplay():
    def __init__(self):
        self.minValue = 0
        self.maxValue = None
        self.number = 0
    
    def setMaxValue(self, maxValue_in):
        self.maxValue = maxValue_in
        self.generateTheNumber()
    
    def generateTheNumber(self):
        self.number = random.randint(self.minValue, self.maxValue);
    
    def start(self):
        while(1):
            print("Type your guess")
            self.onNewGuess()
        
    def onNewGuess(self):
        guess = input()
        print("Teach me how to answer (my number is %i)."%self.number)
        print("----------------")