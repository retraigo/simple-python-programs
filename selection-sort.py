# You can use whatever list you want as long as it is numeric.
myList = [3, 5, 7, 2, 5, 3, 4, 4, 6, 2, 4, 6, 2, 2, 7, 8, 353, 52, 2, 464, 46, 3, 342, 34, 23]

for i in range(len(myList)):
    h = i
    for j in range(i+1, len(myList)):
        if myList[h] > myList[j]:
            h = j              
    myList[i], myList[h] = myList[h], myList[i]
print(myList)
