def rainaverage(l):
    city_dict = {}
    for city, value in l:
        if city in city_dict:
            city_dict[city][0] += value
            city_dict[city][1] += 1
        else:
            city_dict[city] = [value, 1]
    #print(city_dict)

    for city, (total, count) in sorted(city_dict.items()):
            city_dict[city] = total / count
    print(city_dict)

#rainaverage([(1,2),(1,3),(2,3),(1,1),(3,8)])
#another better solution
# def rainaverage(l):
#   raindata = {}
#   for (c,r) in l:
#     if c in raindata.keys():
#       raindata[c].append(r)
#     else:
#       raindata[c] = [r]
#   outputlist = []
#   for c in sorted(raindata.keys()):
#     thisaverage = sum(raindata[c])/len(raindata[c])
#     outputlist.append((c,thisaverage))
#   return(outputlist)

def listtype(l):
  return(type(l) == type([]))
# def flatten(l):
#     if not (listtype(l)):
#         return([l])
#     flatlist = []
#     for e in l:
#         flatlist.extend(flatten(e))
#     return(flatlist)

#another solution
def flatten(l):
    flattened_list = []
    for item in l:
        if isinstance(item, list):
            flattened_list.extend(flatten(item))
        else:
            flattened_list.append(item)
    print(flattened_list)


a = [1,2,[3,4,[5,6]]]
flatten(a)






