ability = list(map(int, input().split()))

answer = 10**18

for i in range(6):
    for j in range(i+1, 6):
        rest = []
        
        for p in range(6):
            if p != i and p !=j :
                    rest.append(p)
        for a in range(4):
            for b in range(a+1, 4):
                team1 = ability[i]+ ability[j]
                team2 = ability[rest[a]] + ability[rest[b]]
                team3 = sum(ability) - team1 -team2
                diff = max(team1, team2, team3) - min(team1, team2, team3)
                answer = min(answer, diff)

print(answer)
