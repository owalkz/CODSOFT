def main():
    while True:
        try:
            arithmetic_expression = input(
                "Enter two numbers with the operand between. (x + y OR x - y OR x * y OR x / y)"
            )
            num1, sign, num2 = arithmetic_expression.split(" ")
            break
        except ValueError:
            print("Please enter the expression in the correct format (x OP y)")

    num1 = int(num1)
    num2 = int(num2)
    if sign == "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    elif sign == "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    elif sign == "/" and num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    elif sign == "/" and num2 == 0:
        print("Division by Zero Error!")
    elif sign == "*":
        print(f"{num1} * {num2} = {num1 * num2}")


if __name__ == "__main__":
    main()
