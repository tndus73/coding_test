A_mat, A_eng = map(int, input().split())
B_mat, B_eng = map(int, input().split())

if A_mat > B_mat:
    print('A')
elif A_mat == B_mat:
    if A_eng > B_eng:
        print('A')
    else:
        print('B')
else:
    print('B')