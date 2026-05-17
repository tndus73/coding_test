M, D = map(int, input().split())

def is_TF(M,D):
    if M in (1,3,5,7,8,10,12):
        if D <= 31:
            return True
    elif M == 2:
        if D <= 28:
            return True
    elif M in (4,6,9,11):
        if D <= 30:
            return True
    else:
        return False

if is_TF(M,D):
    print('Yes')
else:
    print('No')

# Please write your code here.