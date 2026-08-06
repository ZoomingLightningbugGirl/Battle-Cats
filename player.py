from cards import Cards, Buff, Debuff
from newenemy import Enemy
import random
class Player:
    def __init__(self, damage,mana):
        self.damage = damage
        self.health = 100
        self.mana = mana
        self.buff = 0
        self.debuff = 0
        self.deck = []
        self.hand = []
        self.choices = []

    def deal_damage(self, index,target_enemy):
        if index < 0 or index >= len(self.choices):
            return 0

        card = self.choices[index]

        if self.mana >= card.mana:
            self.mana = card.spending(self.mana)
            card.apply()
            
            if isinstance(card, Buff):
                self.buff = card.buff  
            elif isinstance(card, Debuff):
                target_enemy.debuff = card.debuff 
            
            total_damage = self.damage + self.buff
            target_enemy.receiveHit(total_damage)
            self.start_turn()
            
            return total_damage
        else:
            print("Not enough mana!")
            return 0
        def generate_card(self):
            card_type = random.choice([Buff, Debuff])
            mana_cost = random.randint(3, 8)
        
            if card_type == Buff:
                starting_Buff = 10
                return Buff(mana=mana_cost,buff= starting_buff,debuff = 0)
            else:
                starting_debuff = 10
            return Debuff(mana=mana_cost, buff=0, debuff=starting_debuff)
    def start_turn(self):
      
        self.mana += 10
        
        self.choices = []
        for _ in range(3):
            random_card = self.generate_card()
            self.choices.append(random_card)


    