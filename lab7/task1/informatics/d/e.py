n = int(input())
a = [int(i) for i in input().split()]
c = False

for i in range(n-1):
    if a[i]>0 and a[i+1]>0 or a[i]<0 and a[i+1]<0:
        c = True
        break

print("YES" if c else "NO")