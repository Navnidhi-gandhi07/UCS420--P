#4. Loops
#4.1 Write a program to print numbers from 1 to 10 using a for loop.
#4.2 Write a program to print numbers from 1 to 10 using a while loop.
#4.3 Write a program to calculate the sum of numbers from 1 to 100 using a loop.


#4.1 Write a program to print numbers from 1 to 10 using a for loop.
n=int(input("enter the value of n "))
for i in range(1,n+1):
   print(i,end=" ")


#4.2 Write a program to print numbers from 1 to 10 using a while loop.
i=1
while i<=10:
    print(i,end=" ")
    i=i+1


#4.3 Write a program to calculate the sum of numbers from 1 to 100 using a loop.
sum=0
for i in range(1,101):
    sum=sum+i
    
print(sum)
