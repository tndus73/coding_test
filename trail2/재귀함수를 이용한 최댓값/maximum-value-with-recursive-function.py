n = int(input())
arr = list(map(int, input().split()))

def maxT(a):
    if a == 0:
        return arr[0]
    return max(maxT(a-1),arr[a])
print(maxT(n-1))
# Please write your code here.