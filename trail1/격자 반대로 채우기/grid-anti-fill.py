n = int(input())

arr = [[0 for _ in range(n)] for _ in range(n)]
cnt = 0

for i in range(n-1,-1,-1):
    if (n-1-i) % 2 ==0:
        for j in range(n-1, -1, -1):
            cnt +=1
            arr[j][i] = cnt
    else:
        for j in range(n):
            cnt+=1
            arr[j][i] = cnt

for row in arr:
    print(*row)