# Q. Create a two-dimensional array scores as shown in the previous slide and retrieve a few values using indexing.
# Q. Find largest and the smallest score from the 2D list.

scores = [[1,3,5], [6,7,10]]

# # Q1

# for score in scores:
#     for index in score:
#         print(index)
# for i in range(len(scores)):
#     for j in range(len(scores[0])):
#         print(scores[i][j])

min = scores[0][0]
max = scores[0][0]
for score in scores:
    for index in score:
        if min > index:
            min = index
        if max < index:
            max = index
print("The mininum value was {} and the maximum value was {}".format(min, max))