n = int(input())
arr = [int(input()) for _ in range(n)]

cnt = 1
answer = 1

for i in range(1, n):
    if arr[i] > arr[i-1]:
        cnt += 1
    else:
        cnt = 1
    answer = max(cnt, answer)
print(answer)