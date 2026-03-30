def solution(s):
  #  answer = []
    count = 0
    removed = 0
    
    while s != "1":
        zero_cnt = s.count('0')
        removed += zero_cnt
        
        s = s.replace('0','')
        c = len(s)
        
        s = bin(c)[2:]
        count +=1
    return [count,removed]