def solution(n):
    #숫자는 sort() 사용못함, 리스트에서만 사용 가능
    answer = []
    for i in str(n)[::-1]:
        answer.append(int(i))
    return answer