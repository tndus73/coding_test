'''
()개수가 같아야함
def solution(s):
    count = 0

    for ch in s:
        if ch == '(':
            count += 1
        else:
            count -= 1

        if count < 0:
            return False

    return count == 0
'''

def solution(s):
    stack = []
    
    for x in s:
        if x == "(":
            stack.append(x)
        else:
            if not stack:
                return False
            stack.pop()
    
    return len(stack) == 0