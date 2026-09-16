sword_recipe={"Wood":{"cost":{"Wood":3},"durability":59,"damage":4},                                #Recipe For Tiers of Sword
              "Stone":{"cost":{"Wood":1,"Stone":2},"durability":131,"damage":5},
              "Iron":{"cost":{"Wood":1,"Iron":2},"durability":250,"damage":6},
              "Diamond":{"cost":{"Wood":1,"Diamond":2},"durability":1561,"damage":7}}               #Recipe For Items to Smelt
smelt_recipe={"Iron":{"cost":{"Iron Ore":1,"Coal":1}},
              "Charcole":{"cost":{"Wood":1,"Coal":1}}}

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
    def __init__(self,name: str,hp=100) -> None:
        super().__init__(name,hp)
        self.damage_amount=20                                           #Base Damage Amount For Player (Fist)
        self.xp=0                                                       #Starting X
        self.inventory=Inventory()
        self.equipped=None

    def equip(self,tier):
        if tier in self.inventory.equipment.keys():
            self.equipped=tier
        else:
            print("Weapon Not Available!")
        
    def attack(self, target: Entity) -> None:                           #Damage Given By Player , Inherited from Entity() uses Player Base Damage or Weapon Damage (if available) instead of Entity base damage
            print(f"{self.name} hits {target.name}!")
            self.weapon_equipped=self.inventory.equipment.get(self.equipped)
            if self.weapon_equipped and not self.weapon_equipped.is_broken():
                target.take_damage(self.weapon_equipped.damage)
                self.weapon_equipped.use()
            else:
                target.take_damage(self.damage_amount)

class Mob(Entity):                                                      #Class Mob (name,hp,xp drop), inherites Entity()
    def __init__(self,name: str,hp=100) -> None:
        super().__init__(name,hp)
        self.xp_drop=20                                                 #Base XP Drop

    def attack(self,target: Entity) -> None:
            print(f"{self.name} hits {target.name}!")
            target.take_damage(5)

class Skeleton(Mob):                                                    #Class Skeleton (name,hp,xp drop)
    def __init__(self,name: str,hp=100) -> None:
        super().__init__(name,hp)
        self.xp_drop=30

    def attack(self, target: Entity) -> None:                           #Damage Given By Skeleton
        print(f"{self.name} hits {target.name}!")
        target.take_damage(10)

class Utility():
    def __init__(self,name: str,durability: int) -> None:
        self.name=name
        self.durability=durability

    def use(self):
        self.durability-=1

    def is_broken(self):
        return not self.durability>0

class Weapon(Utility):
    def __init__(self,name: str,durability: int,damage: int) -> None:
        super().__init__(name,durability)
        self.damage=damage

class Inventory():                                                                                  #Class Inventory()
    def __init__(self):
        self.resources={"Wood":6,"Stone":3,"Iron":2,"Diamond":3,"Iron Ore":1,"Coal":4}              #Default Inventory
        self.equipment={}                                                                           #Default Equipment

    def add(self,name,quantity):                                                                    #Adding New Resources to self.resources
        if name in self.resources:
            self.resources[name]+=quantity
        else:
            self.resources[name]=quantity

    def craft(self,tier):                                                                           #Crafting
        cost=sword_recipe[tier]["cost"]                                                             #Take Cost Of Crafting from Sword_Recipe
        durability=sword_recipe[tier]["durability"]                                                 #Store Durability and Damage (Later Used when making Weapon())
        damage=sword_recipe[tier]["damage"]
        can_craft=True
        for resource,amount in sword_recipe[tier]["cost"].items():                                  #Check If resources to craft are available in self.resource
            if self.resources[resource]<amount:
                can_craft=False
                break
        if can_craft:
            self.equipment[tier]=Weapon(tier,durability,damage)                                     #Creates Weapon() and store it in self.equipment
            for resource,amount in sword_recipe[tier]["cost"].items():                              #Removes resources from self.resource that where used in crafting
                self.resources[resource] -= amount
        else:
            print(f"Not enought resources to craft a {tier} Sword!")

    def smelt(self,Item):                                                                           #Smelting
        cost=smelt_recipe[Item]["cost"]                                                             #Take Cost of smelting the Item
        can_smelt=True
        for resource,amount in smelt_recipe[Item]["cost"].items():                                  #Check If resources to smelt are available in self.resource
            if self.resources[resource]<amount:
                can_smelt=False
                break
        if can_smelt:
            self.add(Item,1)
            for resource,amount in smelt_recipe[Item]["cost"].items():
                self.resources[resource] -= amount
        else:
            print(f"Not enough resources to smelt {Item}!")

def battle(player: Entity,mobs: list) -> None:                                  #Battle System, stores Mobs in List
    for mob in mobs:                                                            #For each mob in list
        while player.is_alive() and mob.is_alive():                             #Do 1 round
            player.attack(mob)                                                  #Player's Turn
            if not mob.is_alive():
                print(f"{player.name} killes {mob.name}!")
                player.xp+=mob.xp_drop
                print(f"{player.name} now has {player.xp}!")
                break
            mob.attack(player)                                                  #Mob's Turn
            if not player.is_alive():
                print(f"{mob.name} killed {player.name}!")
                return None
    print(f"{player.name} won the battle!")
    

            
def main():
    steve=Player("Steve")
    zombie=Mob("Zombie")
    steve.inventory.craft("Stone")
    steve.equip("Stone")
    battle(steve,[zombie])
    print(steve.inventory.equipment["Stone"].durability)

if __name__=="__main__":
    main()