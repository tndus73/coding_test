'''
def solution(array, commands):
    return [sorted(array[i-1:j])[k-1] for i, j, k in commands]
'''

def solution(array, commands):
    answer = []
    T =[]
    for i, j, k in commands:
        T = array[i-1:j]
        T.sort()
        answer.append(T[k-1])
    
    return answer