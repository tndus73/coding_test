X, Y = map(int, input().split())

answer = 0

for num in range(X,Y+1):
    sumT = 0
    for i in str(num):
        sumT += int(i)
        answer = max(answer, sumT)

print(answer)