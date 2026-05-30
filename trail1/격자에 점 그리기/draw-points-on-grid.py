N, M = map(int, input().split())
arr = [[0 for _ in range(N)] for _ in range(N)]

for i in range(1,M+1):
    r, c = map(int, input().split())
    arr[r-1][c-1] = i

for row in arr:
    print(*row)
