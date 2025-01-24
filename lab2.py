#1. Using input() function take one number from the user and using ternary operators check whether the number is even or odd

number = int(input("Enter a number: "))

# Check if the number is even or odd using a ternary operator
result = "Even" if number % 2 == 0 else "Odd"

# Print the result
print(f"The number {number} is {result}.")

-------------------------------------------------------------------------------------------------------

#2.Take two numbers as input from the user
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Print original values
print(f"Before swapping: num1 = {num1}, num2 = {num2}")

# Swap the numbers
num1, num2 = num2, num1

# Print swapped values
print(f"After swapping: num1 = {num1}, num2 = {num2}")

-------------------------------------------------------------------------------------------------------

#3. Write a Program to Convert Kilometers to Miles 

# Conversion factor
KM_TO_MILES = 0.621371

# Take input from the user in kilometers
kilometers = float(input("Enter distance in kilometers: "))

# Convert kilometers to miles
miles = kilometers * KM_TO_MILES

# Print the result
print(f"{kilometers} kilometers is equal to {miles:.2f} miles.")

-------------------------------------------------------------------------------------------------------

#4. Find the Simple Interest on Rs. 200 for 5 years at 5% per year.

# Given values
principal = 200  # Rs.
rate = 5         # %
time = 5         # years

# Calculate Simple Interest
simple_interest = (principal * rate * time) / 100

# Print the result
print(f"The Simple Interest is Rs. {simple_interest}.")

