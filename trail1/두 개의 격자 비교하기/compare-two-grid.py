N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
arr2 = [list(map(int, input().split())) for _ in range(N)]
newarr = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] != arr2[i][j]:
            newarr[i][j] = 1    

for row in newarr:
    print(*row)