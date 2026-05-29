n, m = map(int, input().split())

arr = [[0 for _ in range(m)] for _ in range(n)]

cnt = 1

for s in range(n+m-1):
    for i in range(n):
        j = s-i

        if 0 <= j < m:
           arr[i][j]= cnt 
           cnt += 1

for row in arr:
    print(*row)