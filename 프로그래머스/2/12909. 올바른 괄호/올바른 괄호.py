def solution(s):
    arr = []
    for str in s:
        if str == '(':
            arr.append(str)
        else:
            if not arr:
                return False
            arr.pop()
    return len(arr) == 0
