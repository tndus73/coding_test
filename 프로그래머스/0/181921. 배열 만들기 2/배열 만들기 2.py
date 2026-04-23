def solution(l, r):
    answer = []
    for num in range(l,r+1):
        ok = True
        for c in str(num):
            if c!= '0' and c!='5':
                ok = False
                break
        if ok:
            answer.append(num)
            
    return answer if answer else [-1]