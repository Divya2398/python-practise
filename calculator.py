# simple calculator

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

select = int(input("Select operations form 1, 2, 3, 4 :"))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if select == 1:
    print(num1, "+", num2, "=",
          add(num1, num2))

elif select == 2:
    print(num1, "-", num2, "=",
          subtract(num1, num2))

elif select == 3:
    print(num1, "*", num2, "=",
          multiply(num1, num2))

elif select == 4:
    print(num1, "/", num2, "=",
          divide(num1, num2))
else:
    print("Invalid input")





