n = int(input())
arr = list(map(int, input().split()))

def makeabs(arr):
    for i in range(len(arr)):
        arr[i] = abs(arr[i])
    return arr

arr = makeabs(arr)

for i in arr:
    print(i, end =' ')
# Please write your code here.