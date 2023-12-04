first_integer = int(input("Enter first integer: "))
second_integer = int(input("Enter second integer: "))
operator = input("Enter operator (+ - * /): ")

if operator == "+":
    result = first_integer + second_integer
elif operator == "-":
    result = first_integer - second_integer
elif operator == "*":
    result = first_integer * second_integer
elif operator == "/":
    if second_integer == 0:
        print("ERROR: Cannot divide by zero")
        result = None
    else:
        result = first_integer / second_integer
else:
    print("Illegal operation")
    result = None

if result is not None:
    print(f"{first_integer}{operator}{second_integer}={result}")
