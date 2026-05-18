A = input()

def difalf(A):
    arr = []
    for i in A:
        arr.append(i)
    arr = set(arr)
    return len(arr)

if difalf(A) == 1:
    print('No')
else:
    print('Yes')

# Please write your code here.