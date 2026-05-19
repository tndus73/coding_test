N = int(input())
arr = list(map(int, input().split()))
answer = []

for i in arr:
    if i % 2 ==0:
        answer.append(i)

print(*answer[::-1])