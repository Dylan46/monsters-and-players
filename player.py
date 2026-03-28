class Player:
    def __init__(self):
        self.weapon = None
        self.health = 100
        self.statusAlive = True  
    def reduceHealth(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            self.statusAlive = False
        else:
            self.statusAlive = True
    
        
player = Player()