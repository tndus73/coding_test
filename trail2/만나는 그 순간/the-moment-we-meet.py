n, m = map(int, input().split())

pos_A = [0]
pos_B = [0]

cur = 0
for _ in range(n):
    d, t = input().split()
    t = int(t)

    for _ in range(t):
        if d == 'R':
            cur +=1
        else:
            cur -=1
        pos_A.append(cur)

cur = 0
for _ in range(m):
    d, t = input().split()
    t = int(t)

    for _ in range(t):
        if d == 'R':
            cur +=1
        else:
            cur -=1
        pos_B.append(cur)

answer = -1

for time in range(1, min(len(pos_A), len(pos_B))):
    if pos_A[time] == pos_B[time]:
        answer = time
        break
print(answer)