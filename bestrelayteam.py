n = int(input())
firstrun = dict()
otherrun = dict()
for i in range(n):
    name, first, other = input().split()
    first = float(first)
    other = float(other)
    firstrun[name] = first
    otherrun[name] = other


sort_names = sorted(otherrun, key = lambda x:otherrun[x])
team = []
time = 0
besttime = firstrun[sort_names[-1]]*100
bestteam = []
for item1 in sort_names:
    team = [item1]
    time = firstrun[item1]
    for item2 in sort_names:
        if item1 == item2:
            continue
        team += [item2]
        time += otherrun[item2]
        if len(team) == 4:
            break
    if time < besttime:
        besttime = time
        bestteam = team

print('{:.9f}'.format(besttime))
print('\n'.join(bestteam))