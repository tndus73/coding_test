MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))


class people:
    def __init__(self, codename='', score=0):
        self.codename = codename
        self.score = score

agents = []

for i in range(MAX_N):
    agents.append(people(codenames[i], scores[i]))

min_agent = agents[0]

for i in range(1, MAX_N):
    if agents[i].score < min_agent.score:
        min_agent = agents[i]

print(min_agent.codename, min_agent.score)
    # Please write your code here.
