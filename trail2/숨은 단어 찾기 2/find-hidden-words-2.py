N, M = map(int, input().split())
arr = [input() for _ in range(N)]

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

target = "LEE"
answer =0

for x in range(N):
    for y in range(M):
        for d in range(8):
            ok =True

            for k in range(3):
                nx = x + dx[d]*k
                ny = y + dy[d]*k

                if not(0<=nx<N and 0<=ny<M):
                    ok = False
                    break
                
                if arr[nx][ny] != target[k]:
                    ok = False
                    break
            
            if ok:
                answer += 1
print(answer)