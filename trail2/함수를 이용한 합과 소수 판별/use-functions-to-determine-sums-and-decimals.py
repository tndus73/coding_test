a, b = map(int, input().split())


def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def is_sum(n):
    if (i%10+i//10) % 2 == 0:
        return True
    return False

cnt = 0
for i in range(a, b+1):
    if is_prime(i) and is_sum(i) :
        cnt +=1
print(cnt)

# Please write your code here.