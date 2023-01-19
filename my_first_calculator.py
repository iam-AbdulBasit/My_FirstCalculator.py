def calculator():
    print("<<<<<<<MY First Calculator>>>>>>>")

def line():
    print("<=><=><=><=><=><=><=><=><=>")

def result():
    print("The result of given value is => ")

num1 = float(input("enter a number: "))
op = input("enter a operator: ")
num2 = float(input("enter anonther number: "))

if op == "+":
    print("The result of given value is => ")
    print(num1+num2)

elif op == "-":
    print("The result of given value is => ")
    print(num1-num2)

elif op == "*":
    print("The result of given value is => ")
    print(num1*num2)

elif op == "/":
    print("The result of given value is => ")
    print(num1/num2)

else:
    print("invalid operation")


calculator()

line()

result()
