myList = ["Apple", "Banana", "Pear", "Orange", "Cherries", "Strawberries"]
looking_for = input("What are you looking for in the list?")
found = False

for i in range (len(myList)):
    if myList[i] == looking_for:
        print("This value has been found at the number {} index".format(i))
        found = True
        break

if found == False:
    print("The item was not found.")