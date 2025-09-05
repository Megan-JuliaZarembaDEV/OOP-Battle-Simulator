from enemy import Enemy 

class baby_elf(Enemy):
    def cry():
        print("waa-waa")

    def take_damage(self, damage):
        print("Why are you hitting a baby, monster!!")
        return super().take_damage(damage)