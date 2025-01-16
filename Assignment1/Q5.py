#5. Data Structures
#5.1 Create a list of 5 numbers. Write a program to find the largest and smallest
#numbers in the list.
#5.2 Create a dictionary with at least 3 key-value pairs. Write a program to retrieve
#the value of a given key.
#5.3 Write a program to sort a list of numbers in ascending and descending order.
#5.4 Write a program to merge two dictionaries into one.


#5.1 Create a list of 5 numbers. Write a program to find the largest and smallest
#numbers in the list.
number=[27,39,72,49,23]
largestelement=max(number)
smallestelement=min(number)
print("the largest value :",largestelement)
print("the smallest value :",smallestelement)


#5.2 Create a dictionary with at least 3 key-value pairs. Write a program to retrieve
#the value of a given key.
dictionary={ "name":"Navnidhi","Branch":"Computer Science","Subject":"Cognitive Computing"}
key=input("enter the key ")
value=dictionary.get(key,"key not present in dictionary")
print("the value of key retrieved :",value)


#5.3 Write a program to sort a list of numbers in ascending and descending order.
number=[27,39,72,49,23]
number.sort()
print("the  ascending order:",number)
number.reverse()
print("the descending order:",number)


#5.4 Write a program to merge two dictionaries into one.
dictionary1={ "name":"Navnidhi","Branch":"Computer Science","Subject":"Cognitive Computing"}
dictionary2={ "age":"18","Rollno":"102317298","Code":"UCS420"}
merged_dictionary=dictionary1|dictionary2
print(merged_dictionary)









