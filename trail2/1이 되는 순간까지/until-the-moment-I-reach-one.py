N = int(input())
cnt = 0

def fact(N):
    global cnt
    if N == 1:
        return cnt
    cnt +=1
    if N % 2 ==0:
        return fact(N//2)
    else:
        return fact(N//3)

print(fact(N))
# Please write your code here.