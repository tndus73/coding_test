n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]

result = 0
for i in range(n):
    answer = [0] * 1001
    for  j in range(n):
        if i == j:
            continue
        a, b = times[j]
        
        for k in range(a, b):
            answer[k] = 1
    result = max(sum(answer), result)
print(result)
            