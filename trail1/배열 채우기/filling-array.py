arr = list(map(int, input().split()))
answer = []

for i in arr:
    if i == 0:
        break
    answer.append(i)

print(*answer[::-1])