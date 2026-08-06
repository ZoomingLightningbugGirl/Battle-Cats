from cards import Cards, Buff, Debuff
from newenemy import Enemy
import random
import pygame

class Player:
    def __init__(self,mana):
        self.health = 100
        self.mana = mana
        self.buff = 0
        self.debuff = 0
        self.deck = []
        self.hand = []
        self.choices = []

    def deal_damage(self, damage, target_enemy):
        self.mana = card.spending(self.mana)
        card.apply()
        if isinstance(card, Buff):
            self.buff = card.buff  
        elif isinstance(card, Debuff):
            target_enemy.debuff = card.debuff 
        total_damage = damage + self.buff
        target_enemy.receiveHit(total_damage)
        self.start_turn()
        return total_damage
            
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
last_tick = pygame.time.get_ticks()

tophat = pygame.image.load("Tophat.png").convert_alpha() 
tophat = pygame.transform.scale(image, (50, 50))
rizz = pygame.image.load("RizzKit.png").convert_alpha() 
rizz = pygame.transform.scale(image, (50, 50))
angy = pygame.image.load("AngyCat.png").convert_alpha() 
angy = pygame.transform.scale(image, (50, 50))

font = pygame.font.Font(None, 50)

def autism():
    damage = 0
    tophat_cats = [(680, 480)] 
    rizz_kits = [(580, 480)]
    angy_cars = [(480, 480)]
autism()

running = True

while running:
    x = font.render(str(int(mana)), True, (0, 0, 0))
    y = font.render(str(Player.health), True, (0, 0, 0))
    screen.fill((255, 255, 255))
    for cat in tophat_cats:
        screen.blit(tophat, cat)
    for cat in rizz_kits:
        screen.blit(rizz, cat)
    for cat in angy:
        screen.blit(angy, cat)
    screen.blit(x, (100, 100))
    screen.blit(y, (0, 100))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_3:
                print("meow")
                tophat.append((random.randint(400, 700), random.randint(250, 350)))
                player.generate_card()
                damage += 1
            if event.key == pygame.K_2:
                print("meow")
                rizz.append((random.randint(400, 700), random.randint(250, 350)))
                player.generate_card()
                damage += 1
            if event.key == pygame.K_1:
                print("meow")
                angy.append((random.randint(400, 700), random.randint(250, 350)))
                player.generate_card()
                damage += 1
            if event.key == pygame.K_q:
                running = False
            if event.key == pygame.K_SPACE:
                Player.deal_damage(damage, target_enemy)
                autism()
    clock.tick(60)
    player.mana += 1
    current_tick = pygame.time.get_ticks()
    if current_tick - last_tick >= 10000:  # 1000 ms since last
        player.start_turn
        last_tick = current_tick
pygame.quit()
