N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
arr2 = [list(map(int, input().split())) for _ in range(N)]
arr3 = []

for i in range(N):
    row = []
    for j in range(M):
        if arr[i][j] == arr2[i][j]:
            row.append(0)
        else:
            row.append(1)
    arr3.append(row)

for row in arr3:
    print(*row)
    