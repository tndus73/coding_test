n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
arr = [0 for _ in range(201)]

for i, j in segments:
    for a in range(i+100,j+100):
        arr[a] += 1

print(max(arr))
# Please write your code here.