from random import *

# Enemy has a 20% chance of gaining a buff
# Enemy deals between 20 and 30 dmg

def receiveHit(atk):
    hp -= atk

hp = 100
buff = 0
baseAtk = randint(20, 30)
Atk = baseAtk + buff
if randint(0, 10) <= 1:
    buff = 10