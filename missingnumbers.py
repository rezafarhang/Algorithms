from collections import defaultdict

n = int(input())
exited = defaultdict(lambda: 0)
last = 0
for i in range(n):
    x = int(input())
    exited[x] = x
    if i == n - 1:
        last = x

flag = False
for j in range(1, last + 1):
    if exited[j] == 0:
        flag = True
        print(j)

if flag == False:
    print("good job")
