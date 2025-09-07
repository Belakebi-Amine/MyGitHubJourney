class Car:
    def __init__(self, brand, year):  # constructor
        self.brand = brand
        self.year = year

    def drive(self):  # method (renamed for clarity)
        print(f"The {self.brand} ({self.year}) is driving")

car1 = Car("Golf", 2025)
car2 = Car("Toyota", 1999)

car1.drive()
car2.drive()


class BankAccount:
    def __init__(self, owner, balance=0):  # balance starts at 0 by default
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):  # method
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):  # method
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
        else:
            print("Not enough funds! Get a job 😆")

    def show_balance(self):  # method
        print(f"{self.owner} has {self.balance} in the account.")


# Test
acc1 = BankAccount("Amine")   # balance defaults to 0
acc1.deposit(20000)
acc1.withdraw(3000)
acc1.show_balance()

class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def attack(self, other):
        other.hp -= 10
        print(f"{self.name} attacked {other.name}! {other.name} now has {other.hp} hp.")

    def is_alive(self):
        if self.hp > 0:
            print(f"{self.name} has {self.hp} hp → alive ✅")
        else:
            print(f"{self.name} has {self.hp} hp → dead ❌")


# Test
ch1 = Character("Amine", 200)
ch2 = Character("Naruto", 10)

ch2.attack(ch1)   # Naruto attacks Amine
ch1.is_alive()

ch1.attack(ch2)   # Amine attacks Naruto
ch2.is_alive()
