n = int(input())
h = [int(input()) for _ in range(n)]

answer = 0

for i in range(max(h)):
    cnt = 1
    arr = []
    for j in range(n):
        if h[j] > i:
            arr.append(j)
    for k in range(1,len(arr)):
        if arr[k]-arr[k-1] > 1:
            cnt +=1
    answer = max(answer, cnt)
print(answer)