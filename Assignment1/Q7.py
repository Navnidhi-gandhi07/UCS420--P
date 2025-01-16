#7. File Handling
#7.1 Write a program to create a text file, write some text into it, and then read and
#print the content.
#7.2 Write a program to append text to an existing file and print the updated
#content.
#7.3 Write a program to count the number of lines in a text file.

#7.1 Write a program to create a text file, write some text into it, and then read and
#print the content.
file = open("file1.txt", "w")
file.write("good morning , myself navnidhi'.\n")
with open("file1.ext", "r") as file:
    contentfile = file.read()
    print(" content:\n", contentfile)


#7.2 Write a program to append text to an existing file and print the updated
#content
with open("file1.txt", "a") as file:
    file.write("\n this is cognitive course")

with open("file1.txt", "r") as file:
    updatedcontent = file.read()
    print("appended file content:\n", updatedcontent)

#7.3 Write a program to count the number of lines in a text file.
with open("file1.txt", "r") as file:
    totallines = file.readlines()
    print("total Number of lines in the text file:", len(totallines))

