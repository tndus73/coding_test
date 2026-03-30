def solution(number, k):
    stack = []
    for num in number:
        #지울수있고, 비어있으면 안되고, 작은 숫자 제거
        while k > 0 and stack and stack[-1] < num :
            stack.pop()
            k -= 1
        stack.append(num)
    return ''.join(stack[:len(stack)-k]) #내림차순