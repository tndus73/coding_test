s = input()
alpha = "abcdefghijklmnopqrstuvwxyz"

for i in alpha:
    if i in s:
        print(s.index(i), end= ' ')    #S에서의 위치를 반환하기 위해 index 사용
    else:
        print('-1', end= ' ')