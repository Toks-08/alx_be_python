def perform_operation(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0 or num2 == 0:
            return "Cannot be divided by 0"
        else:
            return num1 / num2
    else:
        return "invalid operation"

