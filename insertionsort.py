def Insertionsort(list):
    for sliceend in range(len(list)):
        pos = sliceend
        while pos > 0 and list[pos] < list[pos - 1] :
            (list[pos],list[pos - 1]) = (list[pos-1], list[pos])
            pos = pos - 1
print(list)
Insertionsort([64,75,21,89,32])