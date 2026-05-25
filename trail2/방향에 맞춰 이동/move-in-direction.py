n = int(input())


x, y = 0, 0
dx = [1,0,-1,0]
dy = [0,-1,0,1]

direct = { 'E' : 0,
            'S' : 1,
            'W' : 2,
            'N' : 3  }

for _ in range(n):
    alp, num = input().split()
    num = int(num)

    idx = direct[alp]

    x += dx[idx] * num
    y += dy[idx] * num

print(x, y)