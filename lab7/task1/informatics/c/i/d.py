x = str(input())
d = str(input())

count = 0

for i in range(len(x)):
    if x[i] == d:
        count += 1

print(count)