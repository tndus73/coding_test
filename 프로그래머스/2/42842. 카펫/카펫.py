# width * height = brown + yellow
# (width-2) * (height-2) = yellow
def solution(brown, yellow):
    total = brown+yellow
    #세로 길이 탐색
    for height in range(1, total+1):
        if total % height == 0:
            width = total//height
            if (width-2)*(height-2) == yellow:
                return [width,height]
