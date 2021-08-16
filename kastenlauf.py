zt = int(input())

for a in range(t):
    n = int(input())
    x, y = [], []
    for b in range(n + 2):
        line = input().split()
        x.append(int(line[0]))
        y.append(int(line[1]))
    visited = [False] * (n + 2)

    result = "sad"
    reachable = [0]
    d = 0
    while len(reachable) != 0:
        node = reachable[0]
        reachable.remove(reachable[0])
        if node == n + 1:
            result = "happy"
        if not visited[node]:
            visited[node] = True
            for i in range(n + 2):
                d = abs(x[i] - x[node]) + abs(y[i] - y[node])
                if d <= 1000 and d != 0:
                    reachable.append(i)

    print(result)