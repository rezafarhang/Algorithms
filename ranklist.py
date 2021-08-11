n, k = map(int, input().split())
table = []
table_dic = dict()

for i in range(n):
    p, t = map(int, input().split())
    table_dic[i + 1] = [p, t]
    table.append([p, 50 - t])

ranking = sorted(table, key=lambda table: (table[0], table[1]), reverse=True)
for i in range(n):
    ranking[i][1] = 50 - ranking[i][1]

counter = 0
for i in range(n):
    if ranking[k - 1] == table_dic[i + 1]:
        counter += 1
print(counter)
