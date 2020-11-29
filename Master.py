import Gameplay

class Master():
    def __init__(self):
        self.playerName = None
        self.minValue = 0
        self.maxValue = 10
        
        self.gameplay = None
    
    def printSeparator(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
    def setGameplay(self, gameplay_in):
        self.gameplay = gameplay_in

    def onStart(self):
        print("Hello! This is Guess A Number game!")
        self.askPlayerName()
        self.askMaxValue()
        self.runGame();
    
    def askPlayerName(self):
        print("What is your name?")
        self.playerName = input()
        print("Hi", self.playerName + "! Let's start!")
        self.printSeparator();

    def askMaxValue(self):
        print("Teach me to set the maximum value. Now it is", str(self.maxValue) + ".")
        self.printSeparator();
        self.gameplay.setMaxValue(self.maxValue)
    
    def runGame(self):
        self.gameplay.start()