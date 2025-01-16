#11. Use of Libraries
#11.1 Write a program to use the math library to calculate the square root of a given
#number.
#11.2 Write a program to use the datetime library to print the current date and time.
#11.3 Write a program to use the os library to list all files in the current directory.


#11.1 Write a program to use the math library to calculate the square root of a given
#number.
import math
number = int(input("Enter a number: "))
squareroot = math.sqrt(number)
print(f"the squareroot of {number} is {squareroot}")

#11.2 Write a program to use the datetime library to print the current date and time
import datetime
a = datetime.datetime.now()
print(f" date and time : {a}")

#11.3 Write a program to use the os library to list all files in the current directory.
import os
files = os.listdir()
print(" all files in the current directory:")
for file in files:
    print(file)

