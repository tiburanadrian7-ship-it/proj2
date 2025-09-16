def find_index(myDict, search):
    positions = []

    for (i, j), value in myDict.items():
        if value == search:
            positions.append(f"Row {i}, Col {j}")

    if positions:
        return f"Number {search} found at " + " and ".join(positions)
    else:
        return "Number not found in the matrix"

myDict = {}
row = int(input("Enter Row: "))
col = int(input("Enter Col: "))

for i in range(row):
    print(f"Row {i}")
    for j in range(col):
        score = float(input(f"Enter Number {j+1}: "))
        myDict[(i, j)] = score

print("Matrix:")
for i in range(row):
    for j in range(col):
        print(myDict[(i, j)], end=" ")
    print()

search = float(input("Search: "))
print(find_index(myDict, search))