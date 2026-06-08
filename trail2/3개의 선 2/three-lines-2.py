n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

lines = []

for v in range(11):
    lines.append(('x',v))
    lines.append(('y',v))

answer = 0

for i in range(len(lines)):
    for j in range(len(lines)):
        for k in range(len(lines)):
            selected = [lines[i], lines[j], lines[k]]

            ok = True

            for x, y in points:
                covered = False

                for typ, val in selected:
                    if typ == 'x' and x == val:
                        covered = True
                    if typ == 'y' and y == val:
                        covered = True
                
                if not covered:
                    ok = False
                    break
            if ok:
                answer = 1

print(answer)