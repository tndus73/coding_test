A, B = map(int, input().split())

print(f"{A//B}.", end="")

A %= B

for _ in range(20):
    A *= 10
    print(A // B, end="")
    A %= B