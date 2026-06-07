N, M, D, S = map(int, input().split())
eat = []
for _ in range(D):
    p, m, t = map(int, input().split())
    eat.append((p, m, t))

sick = []

for _ in range(S):
    person, time = map(int, input().split())
    sick.append((person, time))

answer = 0

for cheese in range(1,M+1):
    possible = True

    for sick_person, sick_time in sick:
        ate_before =False

        for p, m, t in eat:
            if p == sick_person and m == cheese and t < sick_time:
                ate_before = True
        
        if not ate_before:
            possible = False
            break
    
    if possible:
        people = set()

        for p, m, t in eat:
            if m == cheese:
                people.add(p)

        answer = max(answer, len(people))

print(answer)