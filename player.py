from cards import Cards, Buff, Debuff
from newenemy import Enemy
import random
import pygame
import keyboard
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










pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("cat")

image = pygame.image.load("cattt.jpg").convert_alpha() 
image = pygame.transform.scale(image, (100, 100))

cats = [(680, 480)]  

running = True
while running:
    screen.fill((255, 255, 255))
    for cat in cats:
        screen.blit(image, cat)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("meow")
                cats.append((random.randint(0, 700), random.randint(0, 500)))
                generate_card()
            if event.key == pygame.K_q:
                running = False
pygame.quit()
