numbers = [10,5,12,17,22,4,9,1]
count = 0
swaps = 0
passes = 0
swap_boolean = False

while swap_boolean == False:
    while count < len(numbers) - 1:
        if numbers[count] > numbers[count+1]:
            temp = numbers[count]
            numbers[count] = numbers[count+1]
            numbers[count+1] = temp
            swaps = swaps + 1
            print(numbers)
        count = count + 1
    passes = passes + 1
    if swaps > 0:
        count = 0
        swaps = 0
    else:
        swap_boolean = True
print(numbers)
print(passes)