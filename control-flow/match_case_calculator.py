# match_case_calculator.py
# Simple calculator that uses match/case (Python 3.10+)

def get_number(prompt: str) -> float:
    while True:
        try:
            value = input(prompt)
            return float(value)
        except ValueError:
            print("Please enter a valid number.")

def main():
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    op = input("Choose the operation (+, -, *, /): ").strip()

    result = None

    match op:
        case "+":
            result = num1 + num2
        case "-":
            result = num1 - num2
        case "*":
            result = num1 * num2
        case "/":
            if num2 == 0:
                print("Cannot divide by zero.")
                return
            result = num1 / num2
        case _:
            print("Invalid operation. Choose one of: +, -, *, /")
            return

    # If we get here, result is computed
    # If result is whole number, show without trailing .0
    if result is not None:
        if result.is_integer():
            # show as integer
            print(f"The result is {int(result)}.")
        else:
            print(f"The result is {result}.")

if __name__ == "__main__":
    main()