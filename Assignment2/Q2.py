#2. Create a tuple of marks scored as scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45) and
#perform the following operations using tuple functions:
#i. Identify the highest score and its index in the tuple.
#ii. Find the lowest score and count how many times it appears.
#iii. Reverse the tuple and return it as a list.
#iv. Check if a specific score ‘76’ (input by the user) is present in the tuple and
#print its first occurrence index, or a message saying it’s not present.

scores=(45, 89.5, 76, 45.4, 89, 92, 58, 45)


#i. Identify the highest score and its index in the tuple.
highestscore=max(scores)
print("the highest score in scores :",highestscore)
index1=scores.index(highestscore)
print("the index of highest score in scores :",index1)


#ii. Find the lowest score and count how many times it appears.
lowestscore=min(scores)
print("the lowest score in scores :",lowestscore)
count1=scores.count(lowestscore)
print("the count of lowest score in scores :",count1)


#iii. Reverse the tuple and return it as a list.
reversedscore=list(reversed(scores))
print("the list :",reversedscore)

#iv. Check if a specific score ‘76’ (input by the user) is present in the tuple and
#print its first occurrence index, or a message saying it’s not present.

value=int(input("the integer to find:"))
if value in scores:
    index2=scores.index(value)
    print("the first occurence index:",index2)
    
else:print("the integer is not present ")
