def solution(word):
    words = []
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    def dfs(current):
        if len(current) > 5:
            return
        
        if current: #current가 비어있진않다면
            words.append(current)
        
        for v in vowels:
            dfs(current + v)
    
    dfs("") #빈문자열로 시작
    
    words.sort()
    
    return words.index(word) + 1 #리스트에서 그단어가 몇번째인지찾기