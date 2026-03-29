'''정렬
def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for x, y in zip(participant, completion):
        if x != y:
            return x
    return participant[-1] #완주못한 선수가 제일마지막에 있을때
'''
# 해시
from collections import Counter

def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]
    
    