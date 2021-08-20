import sys

n, m = map(int, input().split())
kg = list(map(int, input().split()))

d = {}
for i in range(m):
    fish_num, money = map(int, input().split())
    if money in d:
        d[money] += fish_num
    else:
        d[money] = fish_num

max_money, i = 0, 0
kg.sort(reverse=True)
for f, mo in sorted(d.items(), reverse=True):
    while mo > 0:
        if i >= len(kg):
            print(max_money)
            sys.exit(0)
        max_money += kg[i] * f
        mo -= 1
        i += 1

print(max_money)
