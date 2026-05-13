cnt = 0

while True:
    N = int(input())
    if N % 2 != 0:
        continue
    else:
        print(N//2)
        cnt+=1
    if cnt == 3:
        break