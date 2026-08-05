from sophiaisles import cards
class Player:
    def __init__(self,damage,health,mana):
        self.damage = damage
        self.health = health
        self.mana = mana
    def apply_cards(self,card):
        return cards.buff.apply()
    def deal_damage(self):
        pass

