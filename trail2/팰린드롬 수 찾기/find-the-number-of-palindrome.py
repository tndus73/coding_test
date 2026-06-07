X, Y = map(int, input().split())

answer = 0

for num in range(X,Y+1):
    n = len(str(num))
    snum = str(num)
    ok = True

    for k in range(n//2):
        if snum[k] != snum[n-1-k]:
            ok = False
            break
    if ok:
        answer += 1

print(answer)