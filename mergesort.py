def merge(A,B):
    (C,m,n) = ([],len(A),len(B))
    (i,j) = (0,0)
    while i+j < m+n:
        if i == m:
            C.append(B[j])
            j += 1
        elif j == n:
            C.append(A[i])
            i += 1
        elif A[i] <= B[j]:
            C.append(A[i])
            i += 1
        elif A[i] > B[j]:
            C.append(B[j])
            j += 1
    print(C)
#merge function that takes two input lists A and B, and returns a new list C that contains all the elements from A and B, sorted in ascending order.

def mergesort(A): #mergesort function that takes an input list A, and returns a new list that contains the elements of A, sorted in ascending order
    if len(A) <= 1:
        print(A)
    else:
        mid = len(A)//2
        L = mergesort(A[:mid])
        R = mergesort(A[mid:])
        print(merge(L,R))

arr = list(range(1,100,2)) + list(range(0,100,2))
mergesort(arr)
