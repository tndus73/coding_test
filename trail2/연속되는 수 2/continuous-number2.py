n = int(input())
arr = [int(input()) for _ in range(n)]
cnt = 1
cntlist = []

for i in range(1, n):
    if arr[i]==arr[i-1]:
        cnt += 1
    else:
        cntlist.append(cnt)
        cnt = 1
cntlist.append(cnt)
print(max(cntlist))