x = int(input())
y = int(input())
z = int(input())
n = int(input())

coordinates = [[i, j, k] for i in range(x) for j in range(y) for k in range(z) if i + j + k != n]

print(coordinates)