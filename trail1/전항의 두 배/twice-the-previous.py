a, b = map(int, input().split())
arr = [a, b]

for i in range(2,10):
    k = arr[i-1] + 2*arr[i-2]
    arr.append(k)
print(*arr)