def solution(array, commands):
    answer = []
    
    for i,j,k in commands:  
        array2 = array[i-1:j] #array에서 i부터j까지 글자뽑아 저장
        array2.sort() #정렬
        answer.append(array2[k-1]) #k번째값(k-1인덱스) 가져와 answer에 넣기
    
    return answer