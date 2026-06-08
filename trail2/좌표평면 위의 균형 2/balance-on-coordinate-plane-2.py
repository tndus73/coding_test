n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

answer = 10**18

for a in range(0, 101, 2):
    for b in range(0, 101, 2):
        k1 = k2 = k3 = k4 = 0

        for x, y in points:
            if x > a and y > b:
                k1 += 1
            elif x > a and y < b:
                k2 += 1
            elif x < a and y > b:
                k3 += 1
            else:
                k4 += 1

        m = max(k1, k2, k3, k4)
        answer = min(answer, m)

print(answer)