n = int(input())
price = list(map(int, input().split()))

answer = []

for i in range(n):
    for j in range(i+1, n):
        if price[j] - price[i] > 0:
            answer.append(price[j]-price[i])
if len(answer) == 0:
    print(0)
else:
    print(max(answer))