T, a, b = map(int, input().split())
listT = [tuple(input().split()) for _ in range(T)]

answer = 0

for k in range(a, b+1):
    dis_s = 10**18
    dis_n = 10**18

    for ch, x in listT:
        if ch == 'S':
            dis_s = min(dis_s, abs(k-int(x)))
        else:
            dis_n = min(dis_n, abs(k-int(x)))
    
    if dis_s <= dis_n:
        answer += 1
print(answer)