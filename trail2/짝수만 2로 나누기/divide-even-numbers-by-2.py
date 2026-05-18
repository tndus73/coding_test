n = int(input())
arr = list(map(int, input().split()))

def even(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i] = arr[i]//2

even(arr)

for i in arr:
    print(i, end =' ')
# Please write your code here.