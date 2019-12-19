# Soldier
class Soldier():
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack():
        return self.strength

    def receive_damage(self, damage):
        self.health = self.health - damage

# Viking
class Viking(Soldier):
    def __init__(self, health, strength, name):
        super().__init__(health, strength)
        self.name = name
    

    def receive_damage(self, damage):
        self.damage = damage
        self.health -= self.damage
        if self.health > 0:
            return f'{self.name} has received {damage} points of damage'
        else:
            return f'{self.name} has died in combat'
    
    def batle_cry():
        return "Odin Owns You All!"
    
# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
        
    
    def receive_damage(self, damage):
        self.damage = damage
        self.health -= self.damage
        if self.health > 0:
            return f'A Saxon has received {damage} points of damage'
        else:
            return 'A Saxon has died in combat'
