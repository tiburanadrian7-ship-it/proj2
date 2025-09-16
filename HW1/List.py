def find_index(myList, search):
    positions = []
    for i in range(len(myList)):
        for j in range(len(myList[i])):
            if myList[i][j] == search:
                positions.append(f"Row {i}, Col {j}")

    if positions:
        return f"Number {search} found at " + " and ".join(positions)
    else:
        return "Number not found in the matrix"

myList = []
row = int(input("Enter Row: "))
col = int(input("Enter Col: "))

for x in range(row):
    print(f"Row {x}")
    innerList = []
    for y in range(col):
        score = float(input(f"Enter Number {y+1}: "))
        innerList.append(score)
    myList.append(innerList)

print("LIST:")
for x in range(len(myList)):
    for y in range(len(myList[x])):
        print(myList[x][y], end=" ")
    print()

search = float(input("Search: "))
print(find_index(myList, search))