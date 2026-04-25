# file = open("scores.txt","r")
# for item in file:
#     print(item.strip()) # Strip removes the space in the print part
# file.close()

# my_scores = []
# file = open("scores.txt","r")
# for item in file:
#     my_scores.append(item)
# file.close()

# main = 0

# for num in my_scores:
#     main = main + int(num)
# print(main)

# file = open("scores.txt","w")
# file.write("Hello world!") # Overwrites the whole file
# file.close()

# file = open("names_scores.txt","x")
# for i in range(5):
#     name = input("Enter there name")
#     file.write(name+"\n")
#     score = input("Enter the score they got")
#     file.write(score+"\n")

file = open("names_scores.txt","r")
Names = []
Scores = []
count = 1
for i in file:
    if count %2 == 1:
        Names.append(i.strip())
        count = count + 1
    else:
        Scores.append(i.strip())
        count = count + 1
print(Names)
print(Scores)

maximum = 0
name = ""

for j in range(len(Scores)):
    if int(Scores[j]) > maximum:
        maximum = int(Scores[j])
        name = Names[j]
print(maximum)
print(name)