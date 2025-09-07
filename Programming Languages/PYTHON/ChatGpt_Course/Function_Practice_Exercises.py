def calculators(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    
    if operation == "-":
        return num1 - num2
    
    if operation == "*":
        return num1 * num2
    
    if operation == "/":
        if num2 ==0:
            print("we can / by 0")
        else:
            return num1 / num2

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def reverse_string(text):
    return text[::-1]

def is_palindrome(word):
    return word == word[::-1]
num1 = input("please entre the first number ")
num2 = input("please entre the second number ")
operation = input("please entre your operation")

print(calculators(num1, num2, operation))
print(factorial(5))  # 120
print(reverse_string("naruto"))  # oturan
print(is_palindrome("level"))   # True
print(is_palindrome("amine"))   # False