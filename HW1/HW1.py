def creatematrix(rows, cols):
    return [{col: float(input(f"Row {row+1} Col {col+1}: ")) for col in range(cols)} for row in range(rows)]

def printmatrix(matrix, rows, cols):
    print("\nThe numbers are:\n")
    for row in range(rows):
        for col in range(cols):
            print(matrix[row][col], end=" ")
        print()

def search(matrix, rows, cols, target):
    return [(row+1, col+1) for row in range(rows) for col in range(cols) if matrix[row][col] == target]



                        # MAIN METHOD
rows, cols = int(input("Enter rows: ")), int(input("Enter cols: "))
matrix = creatematrix(rows, cols)
printmatrix(matrix, rows, cols)

target = float(input("\nSearch: "))
positions = search(matrix, rows, cols, target)

if positions:
    string_pos = [f"Row {row}, Col {col}" for row, col in positions]
    position = " and ".join(string_pos)
    print(f"Number {target} found at {position}")
else:
    print(f"Number {target} not found.")
