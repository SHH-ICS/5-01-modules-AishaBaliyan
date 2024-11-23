# Create a program that will ask the user an addition question. 
# The program will generate two random numbers between 1 and 100, and display them as an addition question with appropriate prompts.
import random
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
print(f"What is {num1} + {num2}?")
input_ans = int(input("Your answer: "))
correct_ans = num1 + num2
if input_ans == correct_ans:
    print("you got the correct answer")
else:
    print(f"This is incorrect. The correct answer is supposed to be {correct_ans}.")
