N = int(input())
SIZE = list(map(int, input().split()))
T, P = map(int, input().split())
result = 0

for i in range(len(SIZE)):
    if SIZE[i]%T == 0:
        result += int(SIZE[i]/T)
    else:
        result += (int(SIZE[i]/T +1))
print(result)

print(N//P, N%P)
