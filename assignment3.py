def remdup(list):
    result = []
    for i in reversed(list): #iterates the list "elements"  in reverse order except the list should be of numbers
        if i not in result:
            result.insert(0,i)
    print(result)

#remdup([1, 2, 3, 2, 4, 3])

# anpther solution to this
# def remdup(l):
#     if len(l) <= 1:
#         return (l)
#
#     if l[0] in l[1:]:
#         return (remdup(l[1:]))
#     else:
#         return ([l[0]] + remdup(l[1:]))
def splitsum(list):
    pos = 0
    neg = 0
    for i in list:
        if i > 0:
            pos += i**2
        else:
            neg += i**3
    print([pos,neg])

#splitsum([1,3,-5])

def matrixflip(l,d):
    outl = []
    for row in l:
        outl.append(row[:])
    if d == 'h':
        for row in outl:
            row.reverse()
    elif d == 'v':
        outl.reverse()
    print(outl)

#matrixflip([[1,2],[3,4]],"v")

