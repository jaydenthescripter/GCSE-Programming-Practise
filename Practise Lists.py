# Q Write a program to take ten numbers as input from the user and add it to a list. Calculate and print the sum of all the numbers in the list.
# Q. Write a Python program to check if a list is empty or not.
# Q. Write a Python program to print the odd numbers from a list of numbers.

# Q. Create a list of five different of foods.
#    Print all list items on one line.
#    Then print each item on a different line.
#    Finally print just the first and fifth item



#1

# count = 0
# total = 0
# numbers = []
# while count < 10:
#     num = int(input("Enter a value"))
#     numbers.append(num)
#     count = count + 1
# print(numbers)
# for number in numbers:
#     total = total + number
# print(total)


#2 

# list = []
# length = len(list)
# if length == 0:
#     print("The list is empty")
# else:
#     print("The list is not empty.")

#3

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for number in numbers:
#     if number % 2 == 1:
#         print(number)
    
#4

# foods = ["Burger", "Pizza", "Calamari", "Chips", "Fish"]
# print(foods)
# for food in foods:
#     print("\n" + food)
# print(foods[0])
# print(foods[4])

#5

scores = []
teams = []
stop = False

while stop == False:
    team = input("Enter a team name or stop ")
    
    if team == "stop":
        stop = True
        break
    score = int(input("Enter that teams score "))
    teams.append(team)
    scores.append(score)

highest = 0
position = 0

# for score_val in scores:
#     if highest <= score_val:
#         highest = score_val


for i in range(len(scores)):
    if highest <= scores[i]:
        highest = scores[i]
        position = i
print(highest)
print(teams[i])