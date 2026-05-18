A = input()

def is_palin():
    if A[:] == A[::-1] :
        return True
    return False

if is_palin():
    print('Yes')
else:
    print('No')
    
# Please write your code here.