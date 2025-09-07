city = "Asaka"
country = "The Land of Woo"

print(f"I Live in {country}, {city}")

a = 15
b = 4

print(a + b)
print(a % b)
print(a ** b)

food = ["tacos", "pizza", "Humberger", "chawerma", "chocolate"]
print(food[1])
food[4] = "ice cream"

for foods in food:
    print(foods)

number = int(input("entre any number"))
if number > 0:
    print("positive number")
elif number < 0:
    print("negative number")
else:
    print("zero")

loop = 10

while loop > 0:
    print(loop)
    loop -= 1
