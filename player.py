from cards import Cards, Buff, Debuff
from newenemy import Enemy
import random
import pygame
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
pygame.font.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("battle cats (plz dont sue me)")

clock = pygame.time.Clock()

tophat = pygame.image.load("Tophat.png").convert_alpha() 
tophat = pygame.transform.scale(image, (50, 50))
rizz = pygame.image.load("RizzKit.png").convert_alpha() 
rizz = pygame.transform.scale(image, (50, 50))
angy = pygame.image.load("AngyCat.png").convert_alpha() 
angy = pygame.transform.scale(image, (50, 50))

mana = 0.0

font = pygame.font.Font(None, 50)

tophat_cats = [(680, 480)] 
rizz_kits = [(580, 480)]
angy_cars = [480, 480)]

running = True

while running:
    x = font.render(str(int(mana)), True, (0, 0, 0))
    screen.fill((255, 255, 255))
    for cat in tophat_cats:
        screen.blit(tophat, cat)
    for cat in rizz_kits:
        screen.blit(rizz, cat)
    for cat in angy:
        screen.blit(angy, cat)
    screen.blit(x, (100, 100))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_3:
                print("meow")
                tophat.append((random.randint(400, 700), random.randint(250, 350)))
                player.generate_card()
            if event.key == pygame.K_2:
                print("meow")
                rizz.append((random.randint(400, 700), random.randint(250, 350)))
                player.generate_card()
            if event.key == pygame.K_1:
                print("meow")
                angy.append((random.randint(400, 700), random.randint(250, 350)))
                player.generate_card()
            if event.key == pygame.K_q:
                running = False
    clock.tick(60)
    player.mana += 0.01
pygame.quit()
