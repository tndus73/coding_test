A, B, C = map(int, input().split())

answer = 0

for i in range(1000):
    for j in range(1000):
        sumT = (A*i) + (B*j) 
        if sumT <= C:
            answer = max(sumT, answer)

print(answer)