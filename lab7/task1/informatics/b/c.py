a = int(input())  
b = int(input()) 

if str(a) == reversed(str(a)) and b == 1:
    print("YES")
elif not str(a) == reversed(str(a)) and b != 1:
    print("YES")
else:
    print("NO")
