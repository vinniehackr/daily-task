#Declare two variables and print that which variable is largest using ternary operators 

a=float(input("Enter the first number:"))
b=float(input("Enter the second number:"))

max_value= a if a>b  else b
print("Largest number is",max_value)
