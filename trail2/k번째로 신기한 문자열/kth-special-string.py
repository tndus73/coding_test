n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]
arr = []

for i in str:
    if i[:len(t)] == t:
        arr.append(i)
arr.sort()
print(arr[k-1])
# Please write your code here.