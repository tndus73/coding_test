def solution(brown, yellow):
    for a in range(3, brown+yellow+1):
        for b in range(3, a+1):
            if a*b == brown+yellow:
                if (a-2)*(b-2) == yellow:
                    return [a,b]
