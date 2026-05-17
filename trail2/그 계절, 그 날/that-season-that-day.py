Y, M, D = map(int, input().split())


def is_TF(Y,M,D):
    if M in (1,3,5,7,8,10,12):
        if D <= 31:
            return True
    elif M in (4,6,9,11):
        if D <= 30:
            return True
    elif M == 2:
        if is_FriTF(Y):
            if D <= 29:
                return True
        else:
            if D <= 28:
                return True
    else:
        return False

def is_FriTF(Y):
    if Y % 4 == 0:
        if Y % 100  == 0:
            if Y % 400 == 0:
                return True
            return False
        return True
    else:
        return False

if is_TF(Y,M,D):
    if M in (3,4,5):
        print('Spring')
    elif M in (6,7,8):
        print('Summer')
    elif M in (9,10,11):
        print('Fall')
    elif M in (12,1,2):
        print('Winter')
    else:
        print('-1')
else:
    print('-1')