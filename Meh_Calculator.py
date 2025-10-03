def add(a, b): 
    return a + b
def subtract(a, b):
    return a - b
def multiply(a ,b):
    return a * b
def divide(a, b):
    return a/b
print("Ughhhhhhhhh, I guess welcome to the Meh-calculator. I guess we have to do math.")
a = float(input("Enter the first number: "))
b = float(input("Hurray up and enter your second number: "))
operation = input("What do you want to do?!?! (+, -, *, /):")
if operation == "+":
    result = add(a, b)
    print(f"Fineeeeee. The sum is {result}. Happy now?")
elif operation == "-":
    result = subtract(a, b)
    print(f"Okay. The difference is {result}. Are we done now?")
elif operation == "*":
    result = multiply (a, b)
    print(f"Greattttttttt.... The product is {result}. Can I sleep now?")
elif operation == "/":
    if b == 0:
        print("WOWWWWW! Did you even go to math or did you skip all the time. That is imposssible")
    else:
        result = divide(a, b)
        print(f"Whatever. The quotient is {result}. Are you satisfied now?")
else:
    print("What are you even trying to do. Try again, maybe with a actual operation this time.")