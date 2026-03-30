def solution(arr1, arr2):
    n = len(arr1) #arr1행
    m = len(arr2[0]) #arr2열
    k_len = len(arr2) #arr1열 = arr2행
    
    result = [[0]*m for _ in range(n)] #행열만들기
    
    for i in range(n):
        for j in range(m):
            for k in range(k_len):
                result[i][j] += arr1[i][k]*arr2[k][j]
    return result