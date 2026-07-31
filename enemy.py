from random import *

class Enemy:
    def __init__(self, hp):
        self.hp = hp
        self.baseatkpower = randint(20, 30)
        self.buff = 0
        self.atk = self.baseatkpower + self.buff
    def receiveHit(self, dmg):
        self.hp
        self.buff = 0

    def giveHit(self):
        if randint(0, 10) <= 1:
            self.buff = 10
        self.atk += self.buff

def receiveHit(atk):
    hp -= atk

raccoon = Enemy(100)
mouse = Enemy(10)
rat = Enemy(20)
fox = Enemy(120)
sparrow = Enemy(50)
hawk = Enemy(80)