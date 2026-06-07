X, Y = map(int, input().split())

answer = 0

for num in range(X,Y+1):
    arr = []
    s = str(num)
    for i in set(s):
        arr.append(s.count(i))
    if len(arr) == 2 and 1 in arr:
        answer += 1

print(answer)