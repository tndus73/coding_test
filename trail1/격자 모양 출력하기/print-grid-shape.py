N, M = map(int, input().split())

arr = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    r, c = map(int, input().split())
    arr[r-1][c-1] = r*c

for row in arr:
    print(*row)