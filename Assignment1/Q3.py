#3. If-Else Statements
#3.1 Write a Python program to check if a number is positive, negative, or zero
#using an if-else statement.
#3.2 Write a program to check if a given number is odd or even.


#3.1 Write a Python program to check if a number is positive, negative, or zero
a=int(input("enter the value of a:"))
if(a==0):
    print("the number a is zero")
elif(a>0):
    print("the number a is positive")
else:
 print("the number a is negative")


#3.2 Write a program to check if a given number is odd or even.
a=int(input("enter the value of a:"))
if(a%2==0):
    print("the number a is even ")
else:
 print("the number a is odd")
