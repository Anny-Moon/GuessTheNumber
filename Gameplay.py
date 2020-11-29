class Gameplay():
    def __init__(self):
        self.minValue = 0
        self.maxValue = None
    
    def setMaxValue(self, maxValue_in):
        self.maxValue = None
    
    def start(self):
        while(1):
            print("Type your guess")
            self.onNewGuess()
        
    def onNewGuess(self):
        guess = input()
        print("Teach me to how to answer")
        print("----------------")