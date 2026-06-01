
num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
p.   print(num1-num2)
elif op == "*":
     print(num1*num2)
elif op == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("cannot divide by zero")
else:
    print("invalid operator")

