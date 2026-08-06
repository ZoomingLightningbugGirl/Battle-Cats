class Cards:
    def __init__(self, mana, buff, debuff):
        self.mana = mana
        self.buff = buff
        self.debuff = debuff

    def spending(self, current):
        current -= self.mana
        return current

class Debuff(Cards):
    def __init__(self, mana, buff, debuff):
        super().__init__(mana, buff, debuff)

    def apply(self):
        self.buff += 10
        return self.buff

class Buff(Cards):
    def __init__(self, mana, buff=0, debuff=0):
        super().__init__(mana, buff, debuff)

    def apply(self):
        self.buff += 10
        return self.buff








    