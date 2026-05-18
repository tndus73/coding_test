n, m = map(int, input().split())
A = list(map(int, input().split()))

def divsubsum(m):
    sumT = 0
    while m >= 1:
        sumT += A[m-1] 
        if m % 2 != 0 :
            m -= 1
        else:
            m //= 2       
    return sumT

print(divsubsum(m))


# Please write your code here.