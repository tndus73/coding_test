abilities = list(map(int, input().split()))

answer = 10**18

for i in range(len(abilities)):
    for j in range(i+1, len(abilities)):
        for k in range(j+1, len(abilities)):
            sum1 = abilities[i] + abilities[j] + abilities[k]
            sum2 = sum(abilities) - sum1
            answer = min(answer, abs(sum2-sum1))

print(answer)
