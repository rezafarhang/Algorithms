m, a, b, c = map(int, input().split())
if 2 * m >= a + b + c:
    print("Possible")
else:
    print("Impossible")