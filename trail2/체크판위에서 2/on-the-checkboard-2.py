R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

answer = 0

for x1 in range(1,R-1):
    for y1 in range(1,C-1):
        for x2 in range(x1+1, R-1):
            for y2 in range(y1+1, C-1):
                if grid[0][0] != grid[x1][y1] and grid[x1][y1] != grid[x2][y2] and grid[x2][y2] != grid[R-1][C-1] :
                    answer += 1

print(answer)