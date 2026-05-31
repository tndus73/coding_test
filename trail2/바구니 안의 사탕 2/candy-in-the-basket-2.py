N, K = map(int, input().split())
arr = [0] * 1001
answer = []

for _ in range(N):
    num, p = map(int, input().split())
    arr[p] += num

for c in range(1001):
    answer.append(sum(arr[c-K:c+K+1]))

print(max(answer))