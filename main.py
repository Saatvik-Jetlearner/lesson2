matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
print(matrix)
print(len(matrix))
print(len(matrix[0]))
print(matrix[1][2])

for i in range(0, len(matrix)):
    for j in range(0, len(matrix[0])):
        print(matrix[i][j], end = " ")
    print("\n")

rows = int(input("Enter number of rows - "))
columns = int(input("Enter number of columns - "))
matrix = []

for i in range(rows):
    temp = []
    for j in range(columns):
        x = int(input("Enter your element - "))
        temp.append(x)
        matrix.append(temp)

for i in range(rows):
    for j in range(columns):
        print(matrix[i][j], end = " ")
    print("\n")