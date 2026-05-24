N, M = map(int, input().split())


arr  = [[0 for _ in range(M)] for _ in range(N)]

num  = 1

for i in range(N):
    for j in range(M):
        arr[i][j] = num
        num += 1

for row in arr:
    print(*row) 