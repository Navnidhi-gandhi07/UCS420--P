#10. Command Line Arguments
#10.1 Write a program to accept two numbers as command-line arguments, add
#them, and print the result.
#10.2 Write a program to accept a string as a command-line argument and print its
#length.


#10.1 Write a program to accept two numbers as command-line arguments, add
#them, and print the result.
import sys
sys.argv = ["  Q10.py", "13", "2"]

if len(sys.argv) != 3:
    print("Usage: python Q10.py  ")
else:
    try:
        n1 = float(sys.argv[1])
        n2 = float(sys.argv[2])
        add= n1 + n2
        print(f"The sum of {n1} and {n2} is: {add}")
    except ValueError:
        print("Error: Please provide valid numbers.")
    


#10.2 Write a program to accept a string as a command-line argument and print its
#length.
sys.argv = ["Q10.py", " good morning"]

if len(sys.argv) != 2:
    print("Usage: python Q10.py ")
else:
    inputstring = sys.argv[1]
    stringlength = len(inputstring)
    print(f"The length of the string '{inputstring}' is: {stringlength}")
