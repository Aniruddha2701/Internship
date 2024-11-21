def calculate():
    print("Please select Operation-\n 1. Add \n 2. Subtract\n 3. Multiply\n 4. Divide\n")
    select = int(input("Select operation from 1, 2, 3, 4\n"))
    a = int(input("Enter the quantity of numbers to be calculated:\n"))
    numbers = []
    for i in range(1, a + 1):
        while True:
            num = input("Enter {} number (or press Enter to skip):\n".format(i))
            if num == "":
                numbers.append(None)
                break
            try:
                num = float(num)
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a number or press Enter to skip.")

    operations = {
        1: ("Add", "+", add),
        2: ("Subtract", "-", sub),
        3: ("Multiply", "*", multiply),
        4: ("Divide", "/", division)
    }

    if select in operations:
        name, operator, func = operations[select]
        valid_numbers = [n for n in numbers if n is not None]
        if valid_numbers:
            print(" {} ".format(operator).join(map(str, valid_numbers)), "=", func(*valid_numbers))
        else:
            print("No numbers provided.")
    else:
        print("Invalid Input")

def add(*args):
    return sum(args)

def sub(*args):
    result = args[0]
    for num in args[1:]:
        result -= num
    return result

def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

def division(*args):
    result = args[0]
    for num in args[1:]:
        if num == 0:
            return "Division with '0' is error:"
        result /= num
    return result

calculate()

   
