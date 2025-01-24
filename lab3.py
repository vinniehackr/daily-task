#1. Python program to check leap year 

# Take input from the user
year = int(input("Enter a year: "))

# Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

-------------------------------------------------------------------------------------------------------

#2. Python Program to Find the Largest Among Three Numbers 

#Take three numbers as input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find the largest number using if-else
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Print the largest number
print(f"The largest number among {num1}, {num2}, and {num3} is {largest}.")

-------------------------------------------------------------------------------------------------------

#3. Python Program to Check if a Number is Positive, Negative or 0

# Take a number as input from the user
num = float(input("Enter a number: "))

# Check if the number is positive, negative, or zero
if num > 0:
    print(f"{num} is a positive number.")
elif num < 0:
    print(f"{num} is a negative number.")
else:
    print(f"The number is zero.")
-------------------------------------------------------------------------------------------------------

#4. A toy vendor supplies three types of toys: Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys. The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000. On orders of more than Rs. 100 for key-based toys, a discount of 5% is given, and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500. Assume that the numeric codes 1,2 and 3 are used for battery based toys, key-based toys, and electrical charging based toys respectively. Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after the discount.

# Input product code and order amount

# Marked price= the amount before any discount
product_code = int(input("Enter the product code (1 for Battery-Based, 2 for Key-Based, 3 for Electrical Charging-Based): "))
marked_price = float(input("Enter the order amount: "))

# Calculate the net amount based on the product code and order amount

#discount= reduction on marked price
if product_code == 1:  # Battery-Based Toys
    if marked_price > 1000:
        discount = marked_price * 0.10  # 10% discount
    else:
        discount = 0
elif product_code == 2:  # Key-Based Toys
    if marked_price > 100:
        discount = marked_price * 0.05  # 5% discount
    else:
        discount = 0
elif product_code == 3:  # Electrical Charging-Based Toys
    if marked_price > 500:
        discount = marked_price * 0.10  # 10% discount
    else:
        discount = 0
else:
    print("Invalid product code.")
    discount = 0

# Calculate net amount

# Selling price= the amount after applying discount

selling_price = marked_price - discount

# Display the net amount
if discount > 0:
    print(f"Discount applied: Rs. {discount:.2f}")
print(f"Net amount to pay: Rs. {selling_price:.2f}")

-------------------------------------------------------------------------------------------------------
