N = int(input())

def f(N):
    if N ==1:
        return 0
    if N % 2 == 0:
        return f(N//2) +1
    else:
        return f(N*3+1) +1

print(f(N))
# Please write your code here.