A, B  = map(int, input().split())
prod = 1
for x in range(A, B+1):
    prod *= x
print(prod)