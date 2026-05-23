n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

point = [0] *1000
cur = 0

for a, b in zip(x,dir):
    if b == 'R':
        for i in range(cur,cur+a):
            point[i] += 1
        cur += a    
    else:
        for i in range(cur-1,cur-a-1,-1):
            point[i] += 1
        cur -= a
cnt = 0
for i in point:
    if i > 1:
        cnt += 1
print(cnt)
# Please write your code here.