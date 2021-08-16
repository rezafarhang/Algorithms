r, c = map(int, input().split())
col = []
road = []
for i in range(r):
    line = input()
    for j in range(c):
        col.append(line[j])
    road.append(col)
    col = []

count = 0
i, j = 0, 0
while True:
    if i < 0 or i >= r or j < 0 or j >= c:
        print("Out")
        break
    if count > r * c * 2:
        print("Lost")
        break
    if road[i][j] == 'T':
        print(count)
        break
    elif road[i][j] == 'N':
        i -= 1
    elif road[i][j] == 'S':
        i += 1
    elif road[i][j] == 'W':
        j -= 1
    elif road[i][j] == 'E':
        j += 1
    count += 1
