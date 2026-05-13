arr = []
while True:
    N = int(input())
    if N <20 or N > 29:
        break
    arr.append(N)
    
print(f'{sum(arr)/len(arr):.2f}')