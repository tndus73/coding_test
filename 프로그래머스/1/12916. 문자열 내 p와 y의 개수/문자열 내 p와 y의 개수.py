def solution(s):
    answer = True
    Pcnt = 0
    Ycnt = 0
    
    for i in s:
        if i.upper() == 'P':
            Pcnt+=1
        if i.upper() == 'Y':
            Ycnt+=1
    if Pcnt == Ycnt:        
        return True
    else:
        return False 