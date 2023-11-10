arr = [[8,2], [3,4], [6,4]]
#[8, 2, 3, 4, 6]
arr2 = list(set([j for i in arr for j in i]))
print(arr2)