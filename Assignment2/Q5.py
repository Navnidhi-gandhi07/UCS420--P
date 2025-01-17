#Write a program to rename a key city to a locaƟon in the following dicƟonary.
dictionary={ "name":"navnidhi", "age":"19","salary":"1,00,000","city":"Ludhiana"}

updatedkey = "location"
oldkey = "city"

if oldkey in dictionary:
    dictionary[updatedkey] = dictionary.pop(oldkey)
    print(f"Updated dictionary: {dictionary}")
else:
    print(f"Key  not found in the dictionary.")
