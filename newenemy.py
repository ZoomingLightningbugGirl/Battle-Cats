import random
class Enemy:
    def __init__(self, hp):
        self.hp = hp
        self.baseatkpower = random.randint(20, 30)
        self.buff = 0
        self.debuff = 0  

        self.atk = self.baseatkpower + self.buff

    def receiveHit(self, dmg):
        self.hp -= dmg 
        self.buff = 0

    def giveHit(self):

        if random.randint(0, 10) <= 1:
            self.buff = 10
        else:
            self.buff = 0
            
        raw_damage = self.baseatkpower + self.buff
        
        reduction_multiplier = (100 - self.debuff) / 100
        self.atk = int(raw_damage * reduction_multiplier)
        
        if self.atk < 0:
            self.atk = 0
            
        return self.atk
raccoon = Enemy(100)
mouse = Enemy(10)
rat = Enemy(20)
fox = Enemy(120)
sparrow = Enemy(50)