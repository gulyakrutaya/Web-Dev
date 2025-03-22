def min_num(a, b, c, d):
    return min(a, b, c, d)

a = [int(i) for i in input().split()]
print(min_num(a[0], a[1], a[2], a[3]))