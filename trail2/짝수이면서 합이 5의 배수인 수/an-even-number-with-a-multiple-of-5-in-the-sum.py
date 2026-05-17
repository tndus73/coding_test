n = int(input())

def numTF(n):
    return n % 2 == 0 and (n%10 + n//10) % 5 == 0

if numTF(n):
    print('Yes')
else:
    print('No')


# Please write your code here.