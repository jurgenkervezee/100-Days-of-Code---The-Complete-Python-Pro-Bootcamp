import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

should_continue = True
# ToDo: Program asks the user to type the first number.
# ToDo: Program asks the user to type a mathematical operator (a choice of "+", "-", "*" or "/")
# ToDo: Program asks the user to type the second number.
# ToDo: Program works out the result based on the chosen mathematical operator.
# ToDo: Program asks if the user wants to continue working with the previous result.
# ToDo: If yes, program loops to use the previous result as the first number and then repeats the calculation process.
# ToDo: If no, program asks the user for the fist number again and wipes all memory of previous calculations.
# ToDo: Add the logo from art.py

first_number = 0
while   should_continue:
    if first_number == 0:
        print(art.logo)
        first_number = float(input("Please type the first number: "))
    operator = str(input("type a mathematical operator +, -, * or / : "))
    second_number = float(input("Please type the second number: "))

    result = operations[operator](first_number, second_number)
    print(f"Result =  {result}")

    work_with_result = input("Would you like to continue working using the result of the previous result? yes/no/stop: ")
    if work_with_result == "yes":
        first_number = result
    elif work_with_result == "no":
        first_number = 0
    else:
        should_continue = False
