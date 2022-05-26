# Sort a list using list comprehension
# You can use any list you want as long as it is numeric
myList = [3, 5, 7, 2, 5, 3, 4, 4, 6, 2, 4, 6, 2, 2, 7, 8, 353, 52, 2, 464, 46, 3, 342, 34, 23]
for n in myList:
    myList = [
        *[x for x in myList if n > x],
        *[x for x in myList if n <= x],
    ]
print(myList)
