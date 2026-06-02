str = tuple(input().split())
answer = 0
for i in str:
    answer += len(i)
print(answer)