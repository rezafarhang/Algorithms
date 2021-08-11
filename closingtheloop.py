n = int(input())
blue = []
red = []
for i in range(1, n + 1):
    segment = int(input())
    line = input().split()

    for j in range(segment):
        si = line[j]
        if si[-1] == 'B':
            blue.append(int(si[:-1]) - 1)
        else:
            red.append(int(si[:-1]) - 1)
    blue.sort(reverse=True)
    red.sort(reverse=True)
    k = min(len(blue), len(red))
    print("Case #%d:" % i, sum(blue[:k]) + sum(red[:k]))
    blue.clear()
    red.clear()