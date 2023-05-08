import Addition
import Subtraction
import Multiplication
import Division
import Power
import Sqrt

print("Operations Available.")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Power")
print("6. Square Root")

while True:
    # take input from the user
    choice = input("\nEnter choice:\n1 - Addition\n2 - Subtraction\n3 - Multiplication\n4 - Division\n5 - Power\n6 - Square root")
    

    # check if choice is one of the six options
    if choice in ('1', '2', '3', '4', '5'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", Addition.Add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", Subtraction.Subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", Multiplication.Multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", Division.Divide(num1, num2))

        elif choice == '5':
            print(num1, "^", num2, "=", Power.pow(num1, num2))
            
    elif choice == '6':
        num = float(input("Enter your number: "))
        print(num, "^","1/2", "=", Sqrt.sq(num))
        
    # check if user wants another calculation
    # break the while loop if answer is no
    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation == "no":
        break
    
    else:
        print("Invalid Input")
