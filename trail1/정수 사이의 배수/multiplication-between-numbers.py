A, B = map(int, input().split())
arr = []
for x in range(A, B+1):
    if x % 5 == 0 or x % 7 == 0:
        arr.append(x)
print(sum(arr), f'{sum(arr)/len(arr):.1f}', end =' ')