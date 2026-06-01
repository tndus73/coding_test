n = int(input())

questions = []

for _ in range(n):
    num, cnt1, cnt2 = input().split()
    questions.append((num, int(cnt1), int(cnt2)))

answer = 0

for x in range(1,10):
    for y in range(1,10):
        for z in range(1,10):
            if x == y or x == z or y == z:
                continue
            candidate = str(x) + str(y) + str(z)

            ok = True

            for question, s, b in questions:
                cnt1 = 0
                cnt2 = 0

                for i in range(3):
                    if candidate[i] == question[i]:
                        cnt1 += 1
                    elif candidate[i]  in question:
                        cnt2 += 1
                
                if cnt1 != s or cnt2 != b:
                    ok = False
                    break
            if ok:
                answer += 1

print(answer)

