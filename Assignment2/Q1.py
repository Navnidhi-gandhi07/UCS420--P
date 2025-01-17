#1. Create a List L that is defined as= [10, 20, 30, 40, 50, 60, 70, 80].
#i. WAP to add 200 and 300 to L.
#ii. WAP to remove 10 and 30 from L.
#iii. WAP to sort L in ascending order.
#iv. WAP to sort L in descending order.

L=[10,20,30,40,50,60,70,80]


#i. WAP to add 200 and 300 to L.
L.append(200)
L.append(300)
print("the list after adding 200 & 300:")
print(L)


#ii. WAP to remove 10 and 30 from L.
L.remove(10)
L.remove(30)
print("the list after removing 10 &30:")
print(L)


#iii. WAP to sort L in ascending order.
L.sort()
print("the list after sorting in ascending oder:")
print(L)


#iv. WAP to sort L in descending order.
L.reverse()
print("the list after sorting in descending order:")
print(L)
