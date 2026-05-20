N = int(input())
cnt = 0
arr = []


for i in range(1, 1000):
    if N*i % 5 == 0:
        cnt += 1
    arr.append(N*i)
    if cnt == 2:
        break

print(*arr)
