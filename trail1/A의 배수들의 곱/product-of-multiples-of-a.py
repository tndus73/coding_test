A, B = map(int, input().split())
prod = 1

for x in range(1, B+1):
    if x % A == 0:
        prod *= x

print(prod)
