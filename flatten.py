

unFlat = [[1,2], [3,4] , [5,6,7]]

flattened = []

for x in range(len(unFlat)):
    mini = unFlat[x]
    for i in range(len(mini)):
        flattened.append(mini[i])

print(flattened)