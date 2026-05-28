n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

answer = 0

for x1 in range(n):
    for y1 in range(n-2):
        
        for x2 in range(n):
            for y2 in range(n-2):
                if x1 == x2 and y1 == y2:
                    continue
                if x1 == x2 and not(y1+2<y2 or y2+2<y1):
                    continue

                coin1 = arr[x1][y1] + arr[x1][y1+1] + arr[x1][y1+2]
                coin2 = arr[x2][y2] + arr[x2][y2+1] + arr[x2][y2+2]

                answer = max(answer, coin1+coin2)
print(answer)