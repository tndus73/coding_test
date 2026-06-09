N = int(input())
seat = input()

answer = 0

for i in range(N):
    if seat[i] == '0':
        temp = list(seat)
        temp[i] = '1'

        min_dist = 10**18

        for j in range(N):
            for k in range(j+1, N):
                if temp[j]=='1' and temp[k]=='1':
                    min_dist = min(min_dist, k-j)
        
        answer = max(answer, min_dist)

print(answer)