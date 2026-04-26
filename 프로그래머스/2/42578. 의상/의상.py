def solution(clothes):
    dic = {}
    answer = 1
    for name, kind in clothes:
        if kind in dic:
            dic[kind] +=1
        else:
            dic[kind] = 1
    
    for kind in dic:
        answer *= (dic[kind]+1)
    
    return answer -1