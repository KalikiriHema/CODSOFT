def calculator():
    # Prompt user for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Prompt user for the operation choice
    operation = input("Choose the operation (+, -, *, /): ")

    # Perform the calculation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            return
    else:
        print("Invalid operation choice.")
        return

    # Display the result
    print(f"The result is: {result}")

# Run the calculator
calculator()
