n, m = map(int, input().split())
pairs = [tuple(map(int, input().split())) for _ in range(m)]

dic = {}
for a, b in pairs:
    if a > b:
        a, b = b, a
    if (a,b) not in dic:
        dic[(a,b)] = 0
    dic[(a,b)] += 1

print(max(dic.values()))
    