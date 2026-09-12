class Entity:
    def __init__(self,name: str,hp=100) -> None:
        self.name=name
        self.hp=hp

    def take_damage(self,amount: int) -> None:
        self.hp-=amount
        print(f"{self.name} took {amount} damage, hp now is {self.hp}!")

    def attack(self,target) -> None:
        print(f"{self.name} hits {target.name}!")
        target.take_damage(5)

    def is_alive(self):
        return self.hp>0

class Player(Entity):
    def __init__(self,name: str,hp=100) -> None:
        super().__init__(name,hp)
        self.damage_amount=20
        self.xp=0

    def attack(self, target: Entity) -> None:
        print(f"{self.name} hits {target.name}!")
        target.take_damage(self.damage_amount)

class Mob(Entity):
    def __init__(self,name: str,hp=100) -> None:
        super().__init__(name,hp)
        self.xp_drop=20

    def attack(self,target: Entity) -> None:
            print(f"{self.name} hits {target.name}!")
            target.take_damage(5)

class Skeleton(Mob):
    def __init__(self,name: str,hp=100) -> None:
        super().__init__(name,hp)
        self.xp_drop=30

    def attack(self, target: Entity) -> None:
        print(f"{self.name} hits {target.name}!")
        target.take_damage(10)

def battle(player: Entity,mobs: list) -> None:
    for mob in mobs:
        while player.is_alive() and mob.is_alive():
            player.attack(mob)
            if not mob.is_alive():
                print(f"{player.name} killes {mob.name}!")
                player.xp+=mob.xp_drop
                print(f"{player.name} now has {player.xp}!")
                break
            mob.attack(player)
            if not player.is_alive():
                print(f"{mob.name} killed {player.name}!")
                return None
    print(f"{player.name} won the battle!")
    
def main():
    steve=Player("Steve")
    zombie=Mob("Zombie")
    skeleton=Skeleton("Skeleton")
    mobs=[zombie,skeleton]
    battle(steve,mobs)
        

if __name__=="__main__":
    main()
