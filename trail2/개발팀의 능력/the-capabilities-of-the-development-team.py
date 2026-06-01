arr = list(map(int, input().split()))

answer = 10**18

for i in range(5):
    for j in range(i+1, 5):
        rest = []
        for p in range(5):
            if p != i and p != j:
                rest.append(p)
        
        for a in range(3):
            for b in range(a+1, 3):
                    team1 = arr[i] + arr[j]
                    team2 = arr[rest[a]] + arr[rest[b]]
                    team3 = sum(arr) - team1 - team2
                    if team1 != team2 and team1 != team3 and team2 != team3:
                        minus = max(team1, team2, team3) - min(team1, team2, team3)
                        answer = min(answer, minus)
                  
if answer == 10**18:
    print(-1)
else:
    print(answer)
