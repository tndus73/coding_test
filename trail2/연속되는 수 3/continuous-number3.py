N = int(input())
arr = [int(input()) for _ in range(N)]

cnt = 1
answer = 1

for i in range(1, N):
    if arr[i] * arr[i-1] > 0 :
        cnt += 1
    else:
        cnt = 1
    answer = max(answer, cnt)

print(answer)



        