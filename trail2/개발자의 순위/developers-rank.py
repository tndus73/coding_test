k, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]

answer  = 0

for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            continue

        ok = True

        for game in range(k):
            rank = arr[game]

            if rank.index(i) > rank.index(j):
                ok = False
                break

        if ok:
            answer += 1
print(answer)