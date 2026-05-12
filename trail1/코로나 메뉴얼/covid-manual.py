A_YorN, A_temp = input().split()
B_YorN, B_temp = input().split()
C_YorN, C_temp = input().split()

arr = []

if (A_YorN == 'Y' and int(A_temp) >= 37):
        arr.append('A')
if (B_YorN == 'Y' and int(B_temp) >= 37):
        arr.append('A')
if (C_YorN == 'Y' and int(C_temp) >= 37):
        arr.append('A')

if arr.count('A')>=2:
    print('E')
else:
    print('N')