list = [1,0,12,10,9,15,26,22]


for i in range(1,len(list)):
    temp = list[i]
    j = i - 1
    while j >= 0 and list[j] > temp:
        list[j + 1] = list[j]
        j = j - 1
        print(list)
    list[j+1] = temp
print(list)