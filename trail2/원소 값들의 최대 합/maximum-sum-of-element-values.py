n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

answer = 0

for i in range(1, n+1):
    sumT = 0
    point = i
    for _ in range(m):
        sumT += arr[point]
        point = arr[point]
    answer = max(sumT, answer)

print(answer)
