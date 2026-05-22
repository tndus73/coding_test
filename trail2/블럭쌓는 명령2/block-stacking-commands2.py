n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

arr = [0 for _ in range(n)]

for i, j in commands:
    for a in range(i-1,j):
        arr[a] += 1

print(max(arr))
# Please write your code here.