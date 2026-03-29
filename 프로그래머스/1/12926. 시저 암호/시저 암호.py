'''
1. 대문자/소문자 구별
2. 알파벳 끝에서 다시 처음으로
3. 공백 유지
ord('A') = 65
ord('a') = 97
(ord(i)-ord('A')+n)%26
'''

def solution(s, n):
    answer = ''
    for i in s: #문자열도 한글자씩 꺼냄
        if i == " ":
            answer += " "
        elif i.isupper():
            #대문자만들기위해서 더함
            answer += chr((ord(i)-ord('A')+n)%26 + ord('A'))
        else:
            answer += chr((ord(i)-ord('a')+n)%26 + ord('a'))
        
    return answer