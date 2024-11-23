# Create a program that accepts 2 numbers from the user. 
# Your program will output a random number between the range given by the user.
import random
num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
minimum = min(num1, num2)
maximum = max(num1, num2)
random_number = random.randint(minimum, maximum)
print(f"the random number between {minimum} and {maximum} are: {random_number}")
