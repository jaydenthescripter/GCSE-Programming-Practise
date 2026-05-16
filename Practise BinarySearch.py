myList = ["Apple", "Banana", "Cherries", "Dragon Fruit", "Fig", "Orange"]
looking_for = "bike"
found = False
Upper = len(myList) - 1
Lower = 0
while found == False and Lower <= Upper:
    midpoint = int((Lower + Upper) / 2)
    if myList[midpoint] == looking_for:
        print("Item found in the list.")
        found = True
    elif myList[midpoint] > looking_for:
        Upper = midpoint - 1
    elif myList[midpoint] < looking_for:
        Lower = midpoint + 1
if found == False:
    print("The item was not found in the list.")
    