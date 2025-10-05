a = int(input("First number: "))
b = int(input("Second number: "))
op = input("Operation (+, -, *, /): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b == 0:
        print("You can't divide by zero")
    else:
        print(a / b)
else:
    print("Unknown operation")
