n = int(input())
sequence = list(map(int, input().split()))
arr = []

for idx1, num1 in enumerate(sequence):
    arr.append((num1, idx1))

arr.sort()
answer = [0] * n

for newidx, (num1, idx1) in enumerate(arr):
    answer[idx1] = newidx +1

print(*answer)


# Please write your code here.
