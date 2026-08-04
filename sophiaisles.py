import pygame
import sys
class cards:
    def __init__(self,mana,buff,debuff):
        self.mana = mana
        self.buff = buff
        self.debuff = debuff
    def spending(current,self):
         current -= self.mana
         return current
class attack(cards):    
    damage_buff = 0
    defense_buff = 0
    def __init__(self, mana, buff, debuff):
        self.mana = mana
        self.buff = buff
        self.debuff = debuff
    def apply(self, buff, debuff):
        self.damage_buff -= debuff
        self.damage_buff += buff
class abilities(cards):
    def __init__(self,mana,buff,debuff):
        self.mana = mana
        self.buff = buff
        self.debuff = debuff