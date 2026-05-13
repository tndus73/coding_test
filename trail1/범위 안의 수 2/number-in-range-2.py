arr = []

for _ in range(10):
    x = int(input())
    if 0 <= x <= 200:
        arr.append(x)

print(sum(arr), f'{sum(arr)/len(arr):.1f}', end =' ')