n = int(input())
A = list(map(int, input().split()))

answer = 10**10

for meet in range(n):
    total = 0
    for i in range(n):
        total += abs(meet-i)*A[i]
    answer = min(answer, total)
print(answer)