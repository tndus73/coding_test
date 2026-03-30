'''
i를 문자로 바꾸고 x*3트릭 쓴 후 sort(reverse=true)해서 붙인다

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
'''

def solution(numbers):
    numbers = list(map(str, numbers))
    k = sorted(numbers, key=lambda x: x*3, reverse=True)
    return str(int(''.join(k)))
