#1. Declare a div() function with two parameters. Then call the function and pass two numbers and display their division. 


# Function definition
def div(a,b):
    if b==0:
        return "Division by zero is not possible"
    else:
        return a/b
    # Function call
num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
result=div(num1,num2)
print(f"The division of {num1} by {num2} is: {result}\n")

#2. Declare a square() function with one parameter.Then call the function and pass one number and display the square of that number . 

def square(side):
    return side**2
# Function call
a=float(input("Enter the side of the square: "))
area=square(a)
print(f"The area of the square is: {area}")

#3. Using max() and min() functions display the maximum and minimum of 5 random numbers.

import random
# Generate 5 random numbers
random_numbers=[random.randint(1,100) for i in range(5)]
print(f"Random numbers: {random_numbers}")
# Find the maximum and minimum
max_num=max(random_numbers)
min_num=min(random_numbers)
print(f"Maximum number:{max_num}")
print(f"Minimum number:{min_num}")

# 4. Accept a name from the user and display that in lower case using lower() function 

name=input("Enter your name: ")
print(f"Your name in lower case:{name.lower()}")

#5. Write a lambda function that takes one argument and returns 'Positive' if the number is greater than 0, 'Negative' if it's less than 0, and 'Zero' if it's 0. Test it with different numbers.

# Lambda function definition
check_number = lambda x: 'Positive' if x > 0 else 'Negative' if x < 0 else 'Zero'

# Testing the lambda function with different numbers
numbers = [10, -5, 0, 25, -100]

# Display results
for num in numbers:
    print(f"Number: {num}, Result: {check_number(num)}")
