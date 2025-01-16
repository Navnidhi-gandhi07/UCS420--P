#8. Exception Handling
#8.1 Write a program to handle division by zero using a try-except block.
#8.2 Write a program to handle invalid input (e.g., when the user enters a string
#instead of a number).
#8.3 Write a program to demonstrate the use of finally in exception handling.


#8.1 Write a program to handle division by zero using a try-except block.
try:
    n1 = int(input("enter the  numerator: "))
    n2 = int(input("enter the denominator: "))
    division= n1 / n2
    print("Result of division:", division)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")


#8.2 Write a program to handle invalid input (e.g., when the user enters a string
#instead of a number).
#8.3 Write a program to demonstrate the use of finally in exception handling.
try:
    number = int(input("Enter the number: "))
    print("entered the number", number)
except ValueError:
    print("Error: Invalid input")
  finally:
    print("Execution of the program is completed")
  

  
