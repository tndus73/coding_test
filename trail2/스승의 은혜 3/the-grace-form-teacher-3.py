N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]

answer = 0
for i in range(N):
    temp = gifts[:]
    p, s = temp[i]
    temp[i] = (p // 2, s)

    temp.sort(key=lambda x:(x[0]+x[1]))

    total = 0
    cnt = 0
    for p, s in temp:
        cost = p + s
        if total+cost <= B:
            cnt += 1
            total +=cost
    answer = max(answer, cnt)       
    
print(answer)