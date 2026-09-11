class Entity:
    def __init__(self,name,hp=100):
        self.name=name
        self.hp=hp

    def take_damage(self,amount):
        self.hp-=amount
        print(f"{self.name} took {amount} damage, hp now is {self.hp}!")

    def attack(self,target):
        print(f"{self.name} hits {target.name}!")
        target.take_damage(5)

    def is_alive(self):
        return self.hp>0

class Player(Entity):
    def __init__(self,name,hp=100):
        super().__init__(name,hp)
        self.damage_amount=20
        self.xp=0

    def attack(self, target):
        print(f"{self.name} hits {target.name}!")
        target.take_damage(self.damage_amount)

class Mob(Entity):
    def __init__(self,name,hp=100):
        super().__init__(name,hp)
        self.xp_drop=20

    def attack(self,target):
            print(f"{self.name} hits {target.name}!")
            target.take_damage(5)

def main():
    steve=Player("Steve")
    zombie=Mob("Zombie")
    skeleton=Mob("Skeleton")
    while True:
        steve.attack(skeleton)
        if not skeleton.is_alive():
            print(f"{steve.name} killed {skeleton.name}!")
            steve.xp+=skeleton.xp_drop
            print(f"{steve.name} now has {steve.xp} xp!")
            break
        skeleton.attack(steve)
        if not steve.is_alive():
            print(f"{skeleton.name} killed {steve.name}!")
            break
        

if __name__=="__main__":
    main()