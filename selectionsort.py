l =[32,64,21,75,89]
def Selectionsort(list):
    for start in range(len(list)):
        for i in range(start,len(list)):
            min_posn = start
            if l[i] < l[min_posn]:
                min_posn = i
                (l[start],l[min_posn]) = (l[min_posn],l[start])
    print(list)


Selectionsort(l)


