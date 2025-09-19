num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation = input("choose the operation (+, -, *, /):")

def result(operation):
    match operation:
         case "+":
             return num1 +num2
         case "-":
             return num1 - num2
         case "*":
             return num1 * num2
         case "/":
             if num1 or num2 == 0:
              return None
             else:
                return num1 / num2
         case _:
            return "invalid"


res = result(operation)
if res is None:
    print("Cannot divide by 0")
elif res == "invalid":
    print("Invalid Operation")
else:
    print(f'The result is {res}')
