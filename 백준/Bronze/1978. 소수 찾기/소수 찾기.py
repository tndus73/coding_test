N = int(input())
num = list(map(int, input().split()))
cnt = 0

for i in num:
    if i > 1 :
        for j in range(2, i):
            if i % j == 0:    #나눈 나머지가 0이면 소수가 아님
                break
        else:
            cnt += 1    #나눈 나머지가 0이면 소수

print(cnt)
        
        