def solution(arr):
    answer = []
    for x in arr:
        if not answer or x != answer[-1] :
            answer.append(x)
    return answer