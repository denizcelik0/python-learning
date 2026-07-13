number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
operation =input("Enter the operation (+, -, *, /): ")

if operation == "+":
    result = number1 + number2
elif operation == "-":
    result = number1 - number2
elif operation == "*":
    result = number1 * number2
elif operation == "/":
    result = number1 / number2

print(f"The result is {result}")
