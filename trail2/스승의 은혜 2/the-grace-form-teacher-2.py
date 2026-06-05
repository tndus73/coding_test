N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]

answer = 0

for i in range(N):
    temp = P[:]
    temp[i] //= 2
    temp.sort()
    
    total = 0
    cnt = 0

    for j in range(N):
        if total + temp[j] <= B:
            total += temp[j]
            cnt +=1
    answer = max(answer, cnt)

print(answer)