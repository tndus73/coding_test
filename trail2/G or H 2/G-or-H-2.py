n = int(input())

people = []

for _ in range(n):
    p, alp = tuple(input().split())
    people.append((int(p), alp))

people.sort()
answer = 0

for i in range(n):
    g = 0
    h = 0
    for j in range(i, n):
        if people[j][1] == 'G':
            g += 1
        else:
            h += 1
                
        if g == 0 or h == 0 or g == h:
            length = people[j][0] - people[i][0]
            answer = max(answer, length)

print(answer)