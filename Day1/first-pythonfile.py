# this is my first day of python and start this with full dediction 
# i will do this with full dediacation

print("Hello PANKAJ how are you")

x= 50
y=20
z=(x*y)
print(z)

p=int(input("Enter the first Number"))
q=int(input("Enter the second Number"))

# Simple Calculator Program

# Take first number
num1 = float(input("Enter first number: "))

# Take second number
num2 = float(input("Enter second number: "))

# Show options
print("Select operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter choice (1/2/3/4): ")

if choice == '1':
    print("Result:", num1 + num2)

elif choice == '2':
    print("Result:", num1 - num2)

elif choice == '3':
    print("Result:", num1 * num2)

elif choice == '4':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error! Division by zero not allowed.")

else:
    print("Invalid choice!")
