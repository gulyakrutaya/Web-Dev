n = int(input())
a = [int(i) for i in input().split()]
c = 0

for i in range(1, n-1):
    if a[i]>a[i+1] and a[i]>a[i-1]:
        c +=1

print(c)