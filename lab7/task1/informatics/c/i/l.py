n = str(input())

r = 0

for i in range(len(n)):
    r += int(n[i]) * 2**(len(n)-1-i)

print(r)