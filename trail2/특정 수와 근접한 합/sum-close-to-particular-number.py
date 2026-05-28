N, S = map(int, input().split())
arr = list(map(int, input().split()))

sumT = sum(arr)
answer = 10**18

for i in range(N):
    for j in range(i+1,N):
        T = sumT - arr[i] - arr[j]
        answer = min(answer, abs(T- S))

print(answer)