n = int(input())
numbers = list(map(int, input().split()))

answer = 0

for i in range(n-2):
    for j in range(i+2,n):
        total = numbers[i] + numbers[j]
        answer = max(answer,total)
print(answer)