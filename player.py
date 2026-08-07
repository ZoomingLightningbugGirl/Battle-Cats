# Alex's slight remake It's not done but rn it's actually great and no i did not use AI for it just sometimes how pygame works
import random
import pygame
from cards import Buff, Debuff
from newenemy import Enemy, raccoon, mouse, rat, fox, sparrow

class Player:
    def __init__(self, mana):
        self.health = 100
        self.mana = mana 
        self.buff = 0
        self.debuff = 0
        self.choices = []

    def deal_damage(self, card, target_enemy):
        self.mana = card.spending(self.mana)
        card.apply()
        if isinstance(card, Buff):
            self.buff += card.buff
        elif isinstance(card, Debuff):
            target_enemy.debuff += card.debuff
        base_damage = 20
        total_damage = base_damage + self.buff
        target_enemy.receiveHit(total_damage)
        self.buff = 0
        self.start_turn()
        return total_damage

    def generate_card(self):
        card_type = random.choice([Buff, Debuff])
        mana_cost = random.randint(3, 8)
        if card_type == Buff:
            starting_buff = 10
            return Buff(mana=mana_cost, buff=starting_buff, debuff=0)
        else:
            starting_debuff = 10
            return Debuff(mana=mana_cost, buff=0, debuff=starting_debuff)

    def start_turn(self):
        self.choices = []
        for _ in range(3):
            self.choices.append(self.generate_card())

pygame.init()
pygame.font.init()
pygame.mixer.music.load("track.mp3")
pygame.mixer.music.play(-1)
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("battle cats (plz dont sue me)")
clock = pygame.time.Clock()

font = pygame.font.Font(None, 28)
log_font = pygame.font.Font(None, 34)

# Create an explicit mapping to find the name of the enemy object
enemy_names = {
    raccoon: "Raccoon",
    mouse: "Mouse",
    rat: "Rat",
    fox: "Fox",
    sparrow: "Sparrow"
}

# Instantiate entities
target_enemy = random.choice([raccoon, mouse, rat, fox, sparrow])
enemy_name = enemy_names.get(target_enemy, "Unknown Stray")
enemy_max_hp = target_enemy.hp

player = Player(mana=10)
player.start_turn()

# Secure Image Asset Loader
def load_sprite(filename, color, size=(60, 60)):
    try:
        return pygame.transform.scale(pygame.image.load(filename).convert_alpha(), size)
    except:
        surf = pygame.Surface(size)
        surf.fill(color)
        return surf

# Load game
background = load_sprite("bg.png", (200, 200, 200), (screen_width, screen_height))

debuff_card_img = load_sprite("Tophat.png", (142, 68, 173), (70, 90))
buff_card_img = load_sprite("RizzKit.png", (39, 174, 96), (70, 90))
attack_card_img = load_sprite("AngyCat.png", (192, 57, 43), (70, 90))

# UI Custom Bar Asset Containers
hpbar = load_sprite("hpbar.png", (46, 204, 11), (180, 30))
manna = load_sprite("manna.png", (41, 128, 185), (180, 30))

# Interactive Flow Engine Metrics
player_turn = True
action_log = "Your Turn! Press 1, 2, 3 or Click a card to play."
ai_cooldown_timer = 0
game_over = False

running = True
while running:
 
    if player.health <= 0:
        action_log = "Game over sucker Restart or Q to quit."
        player_turn = False
        game_over = True
    elif target_enemy.hp <= 0:
        action_log = f"VICTORY - {enemy_name} Defeated! Press R to Fight Again."
        player_turn = False
        game_over = True

    # STAGE CANVAS
    screen.blit(background, (0, 0))
    current_enemy_hp = max(0, target_enemy.hp)
    
    #RENDER ENEMY NAME OVERLAY
    name_txt = font.render(f"Fighting: {enemy_name}", True, (0, 0, 0))
    pygame.draw.rect(screen, (240, 240, 240), (310, 40, 180, 30), border_radius=4)
    screen.blit(name_txt, (400 - name_txt.get_width() // 2, 45))
    
    px, py = 50, 40
    screen.blit(hpbar, (px, py))
    player_hp_txt = font.render(f"HP: {player.health}/100", True, (255, 255, 255))
    screen.blit(player_hp_txt, (px + 15, py + 5))
    
    screen.blit(manna, (px, py + 40))
    player_mana_txt = font.render(f"Manna: {player.mana * 10}/100", True, (255, 255, 255))
    screen.blit(player_mana_txt, (px + 15, py + 45))

    #  RENDER ENEMY UI BARS (Positioned on the Right Side) 
    ex, ey = 570, 40
    screen.blit(hpbar, (ex, ey))
    enemy_hp_txt = font.render(f"HP: {current_enemy_hp}/{enemy_max_hp}", True, (255, 255, 255))
    screen.blit(enemy_hp_txt, (ex + 15, ey + 5))
    
    enemy_debuff_txt = font.render(f"Shred: {target_enemy.debuff}%", True, (255, 255, 255))
    pygame.draw.rect(screen, (142, 68, 173), (ex, ey + 40, 180, 25), border_radius=4)
    screen.blit(enemy_debuff_txt, (ex + 15, ey + 43))

    # CENTERED COMBAT HUD ACTION LOG 
    log_overlay = pygame.Surface((700, 45), pygame.SRCALPHA)
    log_overlay.fill((0, 0, 0, 160)) 
    screen.blit(log_overlay, (50, 130))
    log_display = log_font.render(action_log, True, (255, 255, 255))
    screen.blit(log_display, (400 - log_display.get_width()//2, 140))

    #  BUILD AND RENDER THREE CARD HAND CHOICES 
    #  Built every frame so collision rectangles exist during mouse event clicks
    card_rects = [] 
    for idx in range(3):
        cx = 120 + (idx * 210)
        cy = 440
        card_rect = pygame.Rect(cx - 10, cy - 10, 170, 140)
        card_rects.append(card_rect)

    if player_turn and not game_over:
        for idx, card in enumerate(player.choices):
            cx = 120 + (idx * 210)
            cy = 440
            
            is_buff = isinstance(card, Buff)
            card_color = (39, 174, 96) if is_buff else (142, 68, 173)
            pygame.draw.rect(screen, (255, 255, 255), card_rects[idx], border_radius=8)
            pygame.draw.rect(screen, card_color, card_rects[idx], 3, border_radius=8)
            
            if is_buff:
                screen.blit(buff_card_img, (cx, cy))
                card_title = "BUFF CARD"
            else:
                screen.blit(debuff_card_img, (cx, cy))
                card_title = "DEBUFF CARD"
                
            lbl_idx = font.render(f"[{idx+1}] {card_title}", True, card_color)
            lbl_cost = font.render(f"Cost: {card.mana * 10} Manna", True, (80, 80, 80))
            screen.blit(lbl_idx, (cx, cy + 95))
            screen.blit(lbl_cost, (cx, cy + 115))

    pygame.display.flip()

    # OPPONENT AUTOMATED TURNS  LOOP
    if not player_turn and not game_over:
        if ai_cooldown_timer == 0:
            ai_cooldown_timer = pygame.time.get_ticks()
        elif pygame.time.get_ticks() - ai_cooldown_timer > 1000:
            damage_inflicted = target_enemy.giveHit()
            action_log = f"{enemy_name} hit youDealt {damage_inflicted} damage to you."
            player.mana = min(10, player.mana + 2)
            player_turn = True
            ai_cooldown_timer = 0

    #  INTERACTION PLATFORM
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
                
            # Restart Mechanism Engine
            if event.key == pygame.K_r and game_over:
                player = Player(mana=10)
                target_enemy = random.choice([raccoon, mouse, rat, fox, sparrow])
                # Reset health inside target object directly
                if target_enemy == raccoon: target_enemy.hp = 100
                elif target_enemy == mouse: target_enemy.hp = 10
                elif target_enemy == rat: target_enemy.hp = 20
                elif target_enemy == fox: target_enemy.hp = 120
                elif target_enemy == sparrow: target_enemy.hp = 50
                
                enemy_name = enemy_names.get(target_enemy, "Unknown Stray")
                target_enemy.debuff = 0
                enemy_max_hp = target_enemy.hp
                player.start_turn()
                player_turn = True
                game_over = False
                action_log = " Press 1, 2, 3 or Click a card to play."

            if player_turn and not game_over:
                chosen_index = None
                if event.key == pygame.K_1: chosen_index = 0
                elif event.key == pygame.K_2: chosen_index = 1
                elif event.key == pygame.K_3: chosen_index = 2

                if chosen_index is not None and chosen_index < len(player.choices):
                    selected_card = player.choices[chosen_index]
                    if player.mana >= selected_card.mana:
                        total_dmg = player.deal_damage(selected_card, target_enemy)
                        action_log = f"You deployed Card #{chosen_index+1}! Slashed enemy for {total_dmg} DMG."
                        player_turn = False
                    else:
                        action_log = " not enough Manna points"
                        
        # Support point-and-click mouse selection 
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if player_turn and not game_over:
                mouse_pos = pygame.mouse.get_pos()
                for idx, rect in enumerate(card_rects):
                    if rect.collidepoint(mouse_pos):
                        selected_card = player.choices[idx]
                        if player.mana >= selected_card.mana:
                            total_dmg = player.deal_damage(selected_card, target_enemy)
                            action_log = f"You clicked Card #{idx+1} hit enemy for {total_dmg} DMG."
                            player_turn = False


    clock.tick(60)

pygame.quit()
