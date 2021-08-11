from collections import defaultdict

lslen = int(input())
ls = list(map(int, input().split()))

sum = 0
freq_dic = defaultdict(lambda :0)
for i in range(lslen):
    sum += ls[i]
    freq_dic[str(ls[i])] += 1

res = []
for i in range(lslen):
    s = sum - ls[i]
    if s % 2 == 0:
        s = int(s/2)
        if s in ls:
            if (ls[i] == s and freq_dic[str(i)] > 1) or ls[i] != s:
                res += [str(i+1)]

print(len(res))
print(" ".join(res))