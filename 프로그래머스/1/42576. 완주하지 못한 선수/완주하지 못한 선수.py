''' 정답 0 효율성 0
def solution(participant, completion):
    for name in completion:
        if name in participant:
            participant.remove(name)
    return ''.join(participant)
'''
''' Counter 활용
from collections import Counter

def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]
''' 
'''
def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for p, c in zip(participant, completion):
        if p != c:
            return p
    
    return participant[-1]
'''
def solution(participant, completion):
    dic = {}
    for p in participant:
        dic[p] = dic.get(p,0) + 1
    for c in completion:
        dic[c] -= 1
    for name in dic:
        if dic[name] > 0:
            return name
    
    