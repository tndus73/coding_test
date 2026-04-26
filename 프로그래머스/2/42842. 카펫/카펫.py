def solution(brown, yellow):
    for a in range(3, brown+yellow+1): #가로
        for b in range(3, a+1): #세로
            if a * b== brown+yellow:
                if yellow == (a-2) * (b-2):
                     return [a,b]

