# Input five numbers from the user
number1 = float(input("Enter your first number: "))
number2 = float(input("Enter your second number: "))
number3 = float(input("Enter your third number: "))
number4 = float(input("Enter your fourth number: "))
number5 = float(input("Enter your fifth number: "))

# Let number1 as the initial highest number variable
highest_number = number1

# Use only if statements to compare and determine the highest number
if number2 > highest_number:
    highest_number = number2
if number3 > highest_number:
    highest_number = number3
if number4 > highest_number:
    highest_number = number4
if number5 > highest_number:
    highest_number = number5

# Print the highest number
print(f"The highest number is: {highest_number}")
