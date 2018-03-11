class WaitingTime:

    def __init__(self):
        self.car = None
        self.ride = None
        self.wait = None 
        self.length = None
        self.lengthInv = None 
        self.getsBonus = None
        self.score = 0.0

        
    def cmp_lt(x, y):        
        return (x.score < y.score) if hasattr(x, '__lt__') else (not y.score <= x.score)
        
    def __eq__(self, other):
        return self.score == other.score
        
    def setWait(self, aWait):
        self.wait = aWait
        updateScore()
    
    def setBonus(self, aGetsBonus):
        self.getsBonus = aGetsBonus
        updateScore()
        
    def updateScore(self):
        weightedScore = self.wait # + MainClass.rides[Ride].goodness;
        #if self.getsBonus:
        #    weightedScore *=  1.2#MainClass.weight;
        self.score = weightedScore;
