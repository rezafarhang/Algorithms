import math

s = input()
size = len(s)
row = int(math.sqrt(size))
while size % row != 0:
    row -= 1

col = int(size / row)

tanja = []
for i in range(row):
    tan = []
    for j in range(col):
        tan.append([0])
    tanja.append(tan)

c = 0
for i in range(col):
    for j in range(row):
        tanja[j][i] = s[c]
        c += 1

for i in range(row):
    for j in range(col):
        print(tanja[i][j], end="")
