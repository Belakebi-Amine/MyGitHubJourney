def square(num):
    return num * num

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
def greet_user(name, age):
    print(f"Hello {name}, you are {age} years old")
    
num = int(input("please entre a number "))
name = input("please entre your name ")
age = int(input("please enter your age "))

print(square(num))
print(is_even(num))
greet_user(name, age)