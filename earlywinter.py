n, dm = map(int, input().split())
ls = list(map(int, input().split()))

flag = True
for i in range(n):
    di = ls[i]
    if di <= dm:
        print("It hadn't snowed this early in", i, "years!")
        flag = False
        break

if flag:
    print("It had never snowed this early!")