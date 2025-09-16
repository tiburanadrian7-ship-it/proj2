def find_index(myTuple, search):
    positions = []

    for i in range(len(myTuple)):
        for j in range(len(myTuple[i])):
            if myTuple[i][j] == search:
                positions.append(f"Row {i}, Col {j}")

    if positions:
        return f"Number {search} found at " + " and ".join(positions)
    else:
        return "Number not found in the matrix"

row = int(input("Enter Row: "))
col = int(input("Enter Col: "))

temp_list = []

for i in range(row):
    print(f"Row {i}")
    inner_list = []
    for j in range(col):
        score = float(input(f"Enter Score {j+1}: "))
        inner_list.append(score)
    temp_list.append(tuple(inner_list))

myTuple = tuple(temp_list)

print("TUPLE:")
for i in range(row):
    for j in range(col):
        print(myTuple[i][j], end=" ")
    print()

search = float(input("Search: "))
print(find_index(myTuple, search))