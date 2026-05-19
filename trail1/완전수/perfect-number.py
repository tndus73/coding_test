start, end = map(int, input().split())
cnt = 0
for i in range(start, end +1):
    arr = []
    for j in range(1,i):
        if i % j == 0:
            arr.append(j)
    if sum(arr) == i:
        cnt += 1

print(cnt)
# Please write your code here.
