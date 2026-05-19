N = int(input())

def f(N):
    if N == 1:
        return 1
    if N == 2:
        return 2
    return f(N//3)+f(N-1)

print(f(N))
# Please write your code here.