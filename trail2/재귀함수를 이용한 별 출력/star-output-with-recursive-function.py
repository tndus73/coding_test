n = int(input())

def start(n):
    if n == 0:
        return
    start(n-1)
    print('*'*n, end='')
    print()

start(n)
# Please write your code here.