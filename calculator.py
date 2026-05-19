print(" Simple Calculator ")
while True:
    n1 = float(input("Enter first number: "))

    n2 = float(input("Enter second number: "))
    
    operator = input("Choose operation (+, -, *, /): ")
    
    if operator == "+":
        print("Result:", n1 + n2)

    elif operator == "-":
        print("Result:", n1 - n2)

    elif operator == "*":
        print("Result:", n1 * n2)

    elif operator == "/":
        if n2 != 0:
            print("Result:", n1 / n2)
        else:
            print("Cannot divide by zero")

    else:
        print("Invalid operator")

    again = input("Do another calculation? (yes/no): ")

    if again.lower() != "yes":
        print("Calculator closed.")
        break