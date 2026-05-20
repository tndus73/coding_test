N = int(input())
arr = list(map(int, input().split()))

arr2 = []
for i in arr:
    if i % 2==0:
        arr2.append(i)
print(*arr2)