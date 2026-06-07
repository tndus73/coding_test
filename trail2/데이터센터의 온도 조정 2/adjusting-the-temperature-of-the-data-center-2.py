N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]

answer = 0

for k in range(-1000,1002):
    work = 0
    for a, b in ranges:
        if k < a:
            work += C
        elif a <= k <= b:
            work += G
        else:
            work += H
    answer = max(answer, work)

print(answer)