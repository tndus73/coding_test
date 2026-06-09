N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

arr.sort()

answer = 0

for i in range(N):
    cnt = 0
    for j in range(i,N):
        if arr[j]-arr[i] <= K:
            cnt += 1
    answer = max(answer, cnt)

print(answer)