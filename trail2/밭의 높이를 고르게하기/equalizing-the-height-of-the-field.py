N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

answer = 10**18

for start in range(N-T+1):
    cost = 0
    for i in range(start, start+T):
        cost += abs(arr[i]-H)
    answer = min(answer, cost)
print(answer)