A = input()

def is_palin(A):
    if A[:] == A[::-1] :
        return True
    return False

if is_palin(A):
    print('Yes')
else:
    print('No')
    
# Please write your code here.