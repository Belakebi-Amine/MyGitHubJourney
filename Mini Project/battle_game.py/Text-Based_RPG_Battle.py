import random

class Character:
    def __init__(self, name, hp, attack_power, special_power):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack_power = attack_power
        self.special_power = special_power
        self.special_used = False

    def attack(self, other):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        other.hp -= damage
        if other.hp < 0:
            other.hp = 0
        print(f"{self.name} attacked {other.name}, dealing {damage} damage! {other.name} has {other.hp}/{other.max_hp} HP left")

    def special_attack(self, other):
        if not self.special_used:
            damage = self.special_power
            other.hp -= damage
            if other.hp < 0:
                other.hp = 0
            self.special_used = True
            print(f"{self.name} used SPECIAL ATTACK and dealt {damage} damage!")
        else:
            print(f"{self.name} already used their special attack!")

    def heal(self, amount):
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        print(f"{self.name} healed for {amount}. Now at {self.hp}/{self.max_hp} HP")

    def is_alive(self):
        return self.hp > 0


# --- Characters ---
amine = Character("Amine", 120, 20, 50)   
naruto = Character("Naruto", 150, 15, 60) 

# --- Loop ---
while amine.is_alive() and naruto.is_alive():
    action = input("Choose action: [a]ttack, [h]eal, [s]pecial: ")

    if action == "a":
        amine.attack(naruto)
    elif action == "h":
        amine.heal(20)
    elif action == "s":
        amine.special_attack(naruto)
    else:
        print("Invalid choice, you lose your turn!")

    if not naruto.is_alive():
        print("Amine wins against Naruto!")
        break

    naruto.attack(amine)

    if not amine.is_alive():
        print("Naruto wins!")
        break
