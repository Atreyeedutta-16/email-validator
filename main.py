def calculator():
    print("Simple Calculator")
    print("Operations: +  -  *  /  %")
    op = input("Enter operator (+, -, *, /, %): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero"
    elif op == '%':
        if num2 != 0:
            result = num1 % num2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operator!"

    return f"Result: {result}"
print(calculator())
