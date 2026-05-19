N = int(input())
sum = 0

def fact(N):
    global sum
    if N == 0:
        return
    sum += N
    fact(N-1)
    return sum
print(fact(N))
# Please write your code here.