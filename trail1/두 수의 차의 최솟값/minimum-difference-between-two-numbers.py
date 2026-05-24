N = int(input())
arr = list(map(int, input().split()))

minT = abs(arr[0] - arr[1])

for i in range(N):
    for j in range(i+1,N):
        if abs(arr[i] - arr[j]) < minT:
            minT = abs(arr[i] - arr[j])

print(minT)