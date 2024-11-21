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
            num = int(num)
            numbers.append(num)
            break
        except ValueError:
            print("Invalid input. Please enter a number or press Enter to skip.")

if (select == 1):
    print(" + ".join(map(str, [n for n in numbers if n is not None])), "=", add(*[n for n in numbers if n is not None]))
elif (select == 2):
    print(" - ".join(map(str, [n for n in numbers if n is not None])), "=", sub(*[n for n in numbers if n is not None]))
elif (select == 3):
    print(" * ".join(map(str, [n for n in numbers if n is not None])), "=", multiply(*[n for n in numbers if n is not None]))
elif (select == 4):
    print(" / ".join(map(str, [n for n in numbers if n is not None])), "=", division(*[n for n in numbers if n is not None]))
else:
    print("Invalid Input")
   