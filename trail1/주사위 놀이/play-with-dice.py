arr = list(map(int, input().split()))

cnt = [0] * 7

for i in arr:
    cnt[i] += 1

for i in range(1, 7):
    print(f'{i} - {cnt[i]}')
