n, k = map(int, input().split())
listT = []
for _ in range(n):
    pos, char = input().split()
    listT.append((char, int(pos)))

arr = [0]*10001
answer = []
for strT, post in listT:
    if strT == 'G':
        arr[post-1] = 1
    else:
        arr[post-1] = 2

for i in range(10000-k):
    answer.append(sum(arr[i:i+k+1]))

print(max(answer))