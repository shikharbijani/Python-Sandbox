class Entity():
    def __init__(self,name: str,hp=100) -> None:
        self.name=name
        self.hp=hp

    def take_damage(self,amount: int) -> None:
        self.hp-=amount
        self.hp=max(0,self.hp)
        print(f"{self.name} took {amount} damage, hp now is {self.hp}!")

    def attack(self,target) -> None:
        print(f"{self.name} hits {target.name}!")
        target.take_damage(5)

    def is_alive(self):
        return self.hp>0

class Player(Entity):                                                   #Class Player (name,weapon,hp,damage,xp) inherites Entity()
    def __init__(self,name: str,weapon=None,hp=100) -> None:
        super().__init__(name,hp)
        self.damage_amount=20
        self.xp=0
        self.weapon=weapon


    def attack(self, target: Entity) -> None:                           #Damage Given By Player , Inherited from Entity() uses Player Base Damage or Weapon Damage (if available) instead of Entity base damage
        print(f"{self.name} hits {target.name}!")
        if self.weapon and not self.weapon.is_broken():
            target.take_damage(self.weapon.damage)
            self.weapon.use()
        else:
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

class Utility():                                                        #Class Utlity(name,durability) creates a base class for Weapon/Tools
    def __init__(self,name: str,durability: int) -> None:
        self.name=name
        self.durability=durability

    def use(self):                                                      #Reduces Durability by 1 everytimes utility is used
        self.durability-=1

    def is_broken(self):                                                #Checks is tools is broken (used in battle*)
        return not self.durability>0

class Weapon(Utility):                                                  #Class Weapon(name,durability,damage)
    def __init__(self,name: str,durability: int,damage: int) -> None:
        super().__init__(name,durability)
        self.damage=damage


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
    sword=Weapon("Wooden",3,50)
    steve=Player("Steve",sword)
    zombie=Mob("Zombie")
    skeleton=Skeleton("Skeleton")
    mobs=[zombie,skeleton]
    battle(steve,mobs)
        

if __name__=="__main__":
    main()