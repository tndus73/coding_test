'''
짝수번째는 대문자, 홀수번째는 소문자
단어 기준으로 인덱스 초기화!
'''

def solution(s):
    answer = ''
    idx = 0
    
    for i in s:
        if i == ' ':
            answer += ' '
            idx = 0
        else:
            if idx % 2 == 0:
                answer += i.upper()
            else:
                answer += i.lower()
            idx += 1    
    return answer