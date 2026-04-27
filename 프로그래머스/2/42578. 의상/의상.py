def solution(clothes):
    dic = {}
    answer = 1
    for name, kind in clothes:
        if kind not in dic:
            dic[kind] = 1
        else:
            dic[kind] += 1
    for kind, num in dic.items():
        answer *= (num+1)
    return answer-1