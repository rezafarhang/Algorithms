t = int(input())
trees = []
res = []
for i in range(t):
    n, a, b, c, d, x0, y0, m = map(int, input().split())
    x, y = x0, y0
    trees.append((x, y))
    for j in range(1, n):
        x = (a * x + b) % m
        y = (c * y + d) % m
        trees.append([x, y])
    l = len(trees)
    count = 0
    for a in range(l):
        for b in range(a + 1, l):
            for c in range(b + 1, l):
                if (trees[a][0] + trees[b][0] + trees[c][0]) % 3 == 0 and (
                        trees[a][1] + trees[b][1] + trees[c][1]) % 3 == 0:
                    count += 1
    trees = []
    res.append(count)

for i in range(len(res)):
    print("Case #%d: %d" % (i + 1, res[i]))