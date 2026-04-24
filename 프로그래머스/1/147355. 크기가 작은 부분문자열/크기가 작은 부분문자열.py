def solution(t, p):
    answer = []
    count = 0
    for i in range(len(t)-len(p)+1):
        answer.append(t[i:i+len(p)])
    
    for str in answer:
        if int(str) <= int(p):
            count+=1
        
    return count