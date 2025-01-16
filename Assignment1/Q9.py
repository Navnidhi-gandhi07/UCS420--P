#9. Random Numbers
#9.1 Write a program to generate 5 random numbers between 1 and 100 and print
#them.
#9.2 Write a program to generate a random number and check if it is prime.
#9.3 Write a program to simulate rolling a six-sided die.
#9.4 Write a program to shuffle a list of numbers.
#9.5 Write a program to randomly select an item from a list.
#9.6 Write a program to generate a random password of given length.
#9.7 Write a program to pick a random card from a standard deck of 52 cards.


#9.1 Write a program to generate 5 random numbers between 1 and 100 and print
#them.
import random
for i in range(0,5):
    print(random.randint(1, 100))
  

#9.2 Write a program to generate a random number and check if it is prime.
number = random.randint(1, 100)
print("random number:", number)
if num > 1:
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
            break
    if prime:
        print(number, "taken number is a prime number")
    else:
        print(number, "taken number is not a prime number")
 else:
    print(number, "taken number is not a prime number")
   

#9.3 Write a program to simulate rolling a six-sided die.
rollednumber=random.randint(1,6)
print("the rolled out number",rollednumber)


#9.4 Write a program to shuffle a list of numbers.
numbers=[27,49,23,22,21]
random.shuffle(numbers)
print("the shuffled list:", numbers)


#9.5 Write a program to randomly select an item from a list.
numbers=[27,49,23,22,21]
selectednumber=random.choice(numbers)
print("the selected randon number",selectednumber)



#9.6 Write a program to generate a random password of given length.
import string
def passwordcreation(totalcharacters):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(totalcharacters))
    return password

totalcharacters = int(input("Enter the password's total characters : "))
print("Generated password:", passwordcreation(totalcharacters))


#9.7 Write a program to pick a random card from a standard deck of 52 cards.
import random

# Define ranks and suits
number = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
suit = ["Heart", "Diamond", "Club", "Spade"]
randompickedcard = f"{random.choice(number)} of {random.choice(suit)}"

print("Randomly selected card:", randompickedcard)




