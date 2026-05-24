N = list(map(int, input().split()))

maxT = N[0]

for i in range(1, len(N)):
    if N[i] > maxT:
        maxT = N[i]

print(maxT)