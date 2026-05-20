N = int(input())
arr = []
arr.extend([1,N])

for i in range(2,1000):
    k = arr[i-2] + arr[i-1]
    arr.append(k)
    if k > 100:
        break
  
print(*arr)