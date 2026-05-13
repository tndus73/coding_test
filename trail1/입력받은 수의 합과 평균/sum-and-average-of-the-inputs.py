N = int(input())
arr = []

for _ in range(N):
    x = int(input())
    arr.append(x)
print(sum(arr), f'{sum(arr)/len(arr):.1f}')