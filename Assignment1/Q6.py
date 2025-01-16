#6. Strings
#6.1 Write a program to count the number of vowels in a given string.
#6.2 Write a program to reverse a string and print it.
#6.3 Write a program to check if a string is a palindrome.


#6.1 Write a program to count the number of vowels in a given string.
string1 = input("Enter a string: ")
vowels = "aeiouAEIOU"
i = 0
for j in string1:
    if j in vowels:
        i += 1
print("Number of vowels ", i)


#6.2 Write a program to reverse a string and print it.
string1 = input("Enter a string: ")
reversedstring = ''.join(reversed(string1))
print("Reversed string:", reversedstring)


#6.3 Write a program to check if a string is a palindrome.
string1 = input("Enter a string: ")
updatedstring = string1.replace(" ", "").lower()
if updatedstring == updatedstring[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")



