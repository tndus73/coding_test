N = int(input())

def oddeven(N):
    if N == 1:
        return 1

    if N == 2:
        return 2

    return (oddeven(N-2)) + N

print(oddeven(N))
# Please write your code here.