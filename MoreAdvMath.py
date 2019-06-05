print("This is a more advanced calculator.")

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
operator = input("Enter a operator you want to use: ")

if operator == "+":
    numTotal = int(num1) + int(num2)
    print("Your total is: " + str(numTotal))
elif operator == "-":
    numTotal = int(num1) - int(num2)
    print("Your total is: " + str(numTotal))
elif operator == "*":
    numTotal = int(num1) * int(num2)
    print("Your total is: " + str(numTotal))
elif operator == "/":
    numTotal = int(num1) / int(num2)
    print("Your total is: " + str(numTotal))
else:
    print("You have entered either an invalid operator or a not yet emplimented one.")