n = int(input())
arr = list(map(int, input().split()))

cnt = 0

for length in range(1,n+1):
    for start in range(n-length+1):
      if sum(arr[start:start+length])/len(arr[start:start+length]) in arr[start:start+length]:
            cnt += 1
print(cnt)
