n, m = map(str, input().split())

if len(n) > len(m):
    print(n, len(n))
elif len(n) == len(m):
    print('same')
else:
    print(m, len(m))
