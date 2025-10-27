N = int(input())
result = 0
for i in range(1, N+1):
    nums = list(map(int, str(i)))
    K = sum(nums)+i
    if K == N:
        result = i
        break
print(result)
