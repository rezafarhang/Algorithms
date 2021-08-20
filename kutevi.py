import math
n, k = map(int, input().split())
line = input().split()
a = 360
for i in range(n):
    a = math.gcd(int(line[i]), a)

line = input().split()
for i in range(k):
    if int(line[i]) % a == 0:
        print("YES")
    else:
        print("NO")
