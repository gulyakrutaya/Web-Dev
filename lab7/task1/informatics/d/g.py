n = int(input())
a = [int(i) for i in input().split()]
x = 0

for i in range(n//2):
    x = a[i]
    a[i] = a[n-1-i]
    a[n-1-i] = x

for i in range(n):
    print(a[i], end=' ')