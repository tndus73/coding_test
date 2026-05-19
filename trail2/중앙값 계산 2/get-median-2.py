n = int(input())
arr = list(map(int, input().split()))


for i in range(0,n,2):
    listT = arr[:i+1]
    listT.sort()
    print(listT[i//2], end =' ')
# Please write your code here.