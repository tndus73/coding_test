'''
skill에 있는 문자만 뽑는다
→ 순서가 맞는지 확인
'''

def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        filtered = ''
        for ch in tree:
            if ch in skill:
                filtered += ch
        if skill.startswith(filtered):
            answer +=1
    return answer