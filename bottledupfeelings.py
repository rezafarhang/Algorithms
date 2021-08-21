s, v1, v2 = map(int, input().split())
c = int(s / v1)
flag = True

while c >= 0:
    temp = s - (v1 * c)
    if temp % v2 == 0:
        print(c, int(temp / v2))
        flag = False
        break
    else:
        c -= 1

if flag:
    print("Impossible")
