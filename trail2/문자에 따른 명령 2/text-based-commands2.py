dirs = input()
x, y = 0, 0

dx = [0,1,0,-1]
dy = [1,0,-1,0]

dir_num = 0 #북쪽

for alp in dirs:
    if alp =='L':
        dir_num  = (dir_num-1+4)%4
    elif alp == 'R':
        dir_num = (dir_num+1)%4
    elif alp == 'F':
        x += dx[dir_num]
        y += dy[dir_num]

print(x,y)
    
# Please write your code here.