def solution(s):
    answer = 0
    for _ in range(len(s)):
        arr = []
        ok = True
        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                arr.append(ch)
            else:
                if not arr:
                    ok = False
                    break
                if ch == ')' and arr[-1] != '(':
                    ok = False
                    break
                if ch == ']' and arr[-1] != '[':
                    ok = False
                    break
                if ch == '}' and arr[-1] != '{':
                    ok = False
                    break  
                arr.pop() 
        if ok and not arr:
            answer += 1
        s = s[1:] + s[0]
    return answer