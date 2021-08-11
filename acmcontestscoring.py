from collections import defaultdict

status = defaultdict(lambda: 0)
correctpr = []

while True:
    x = input()
    if x == "-1":
        break
    else:
        time, problem, cor = map(str, x.split())
        time = int(time)
        if cor == "right":
            status[problem] += time
            correctpr.append(problem)
        else:
            status[problem] += 20

res = 0
for i in range(len(correctpr)):
    res += status[correctpr[i]]
print(len(correctpr), res)
