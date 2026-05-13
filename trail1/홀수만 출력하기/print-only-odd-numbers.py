N = int(input())

for _ in range(N):
    x = int(input())
    if x % 2 != 0 and x % 3 == 0:
        print(x)