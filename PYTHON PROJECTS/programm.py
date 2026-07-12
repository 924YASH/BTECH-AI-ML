#user friendly calculator for basic calculation
ans = "y"

while ans == "y":
    a = float(input("Enter 1st number: "))
    b = float(input("Enter 2nd number: "))
    operator = input("Choose an operator (+, -, *, /): ")

    if operator == "+":
        print("Addition =", a + b)

    elif operator == "-":
        print("Subtraction =", a - b)

    elif operator == "*":
        print("Multiplication =", a * b)

    elif operator == "/":
        if b != 0:
            print("Division =", a / b)
        else:
            print("Error: Division by zero is not allowed.")

    else:
        print("Invalid operator!")

    ans = input("\nDo you want to calculate again? (y/n): ")

print("Program stopped.")