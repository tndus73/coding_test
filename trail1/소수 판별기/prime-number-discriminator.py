N = int(input())
arr = []

for i in range(2, N+1):
    if N % i == 0:
        arr.append(i)
        
if len(arr) == 1:
    print('P')
else:
    print('C')