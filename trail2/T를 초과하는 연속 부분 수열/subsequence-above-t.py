n, t = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
answer = 0

for i in range(n):
    if arr[i] > t:
        cnt += 1
    else:
        cnt = 0
    answer = max(cnt, answer)

print(answer)
# Please write your code here.