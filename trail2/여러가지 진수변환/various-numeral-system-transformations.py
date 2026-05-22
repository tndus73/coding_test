N, B = map(int, input().split())
arr = []

while True:
    if N < 1:
        break
    arr.append(N%B)
    N //= B
    
for i in arr[::-1]:
    print(i, end ='')
# Please write your code here.