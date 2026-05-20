arr = list(map(int, input().split()))

A = sum(arr[::2])
B = sum(arr[1::2])

print(abs(A-B))
