#WAP to create a list of 100 random numbers between 100 and 900. Count and print
#the:
#i. All odd numbers
#ii. All even numbers
#iii. All prime numbers
import random
count=0
randomlist=[]
for i in range(100):
    randomlist.append(random.randint(100,900))
    count=count+1

print ("the list is:",randomlist)
print("the count:",count)
 
 #i. All odd numbers
count1=0
oddnumbers = []
for j in randomlist:
    if j % 2 != 0:
        oddnumbers.append(j)
        count1=count1+1
print(f"Odd numbers: {oddnumbers}")
print("the count:",count1)


#ii. All even numbers
count2=0
evennumbers = []
for j in randomlist:
    if j % 2 == 0:
        evennumbers.append(j)
        count2=count2+1
print(f"even numbers: {evennumbers}")
print("the count:",count2)


#iii. All prime numbers
count3 = 0
primenumbers = []
for i in oddnumbers: 
    if i > 1:  
        for j in range(2, i):  
            if i % j == 0:  
                break
        else:  
            primenumbers.append(i)
            count3 += 1
print(f"Prime numbers: {primenumbers}")
print("The count:", count3)
