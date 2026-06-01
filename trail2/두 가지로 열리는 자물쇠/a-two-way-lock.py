N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

def close(x, y):
    diff = abs(x-y)
    return min(diff, N-diff) <=2

cnt = 0

for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            if (close(a1,i) and close(b1,j) and close(c1,k)) or (close(a2,i) and close(b2,j) and close(c2,k)):
                cnt +=1

print(cnt)
