from enemy import Enemy

class Bowler(Enemy):
    

     def __init__(self, name, color):
       super().__init__(name)
       self.health = 200
       self.color = color
       self.attack_power = 20

     def attack(self):
        return random.randint(1, self.attack_power)


     def take_damage(self, damage):
        print("heee-hee--hoo!")
        print("bowlinggg.....")
        return super().take_damage(damage)
