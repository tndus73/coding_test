num_list = []

for i in range(9):
    a = int(input())
    num_list.append(a)    #append사용해 리스트에 문자 삽입

print(max(num_list))    #최댓값 max함수 사용
print(num_list.index(max(num_list))+1)    #index로 위치파악(0부터라 +1)