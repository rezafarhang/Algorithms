testcase_number = int(input())
for i in range(testcase_number):
    a, b, c, d = map(int, input().split())
    print(max((a + d) ** 2 + b ** 2 + c ** 2 + 7 * min(a + d, min(b, c)),
              max(a ** 2 + (b + d) ** 2 + c ** 2 + 7 * min(a, min(b + d, c)),
                  a ** 2 + b ** 2 + (c + d) ** 2 + 7 * min(a, min(b, c + d)))))

