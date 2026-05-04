A, B = map(int, input().split())
arr = [A, B]
for _ in range(8):
    arr.append((arr[-2]+arr[-1])%10)

print(*arr)