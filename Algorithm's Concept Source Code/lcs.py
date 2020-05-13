def lcs(x, y):
    m, n = len(x), len(y)
    L = [[0 for a in range(n + 1)] for b in range(m + 1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif x[i - 1] == y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    length = L[m][n]
    print(length if length != 0 else "NO SOLUTION")
    i, j = m, n
    result = []
    while i > 0 and j > 0:
        if x[i-1] == y[j-1]:
            result.append(x[i-1])
            i-=1
            j-=1
        elif L[i-1][j] > L[i][j-1]:
            i-=1
        else:
            j-=1
    print("".join(reversed(result)))


x = input()
y = input()
lcs(y,x)
