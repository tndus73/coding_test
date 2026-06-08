n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]

answer = 0

for start in range(1,4):
    stone = start
    score = 0
    for a, b, c in moves:
        if stone == a:
            stone = b
        elif stone == b:
            stone =a

        if stone == c:
            score += 1
    answer = max(answer, score)

print(answer)

