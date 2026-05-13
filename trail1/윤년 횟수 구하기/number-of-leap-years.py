N = int(input())

for i in range(1, N+1):
    if i % 4 == 0:
        if i % 100 == 0 and i % 400 !=0 :
            N -= 1
    else:
        N -= 1
print(N)