'''
1. 아직 방문 안 한 컴퓨터 하나를 찾고
2. 그 컴퓨터에서 BFS 돌려서
3. 연결된 애들을 전부 방문 처리
4. BFS 한 번 끝나면 네트워크 1개

BFS

from collections import deque

def solution(n, computers):
    visited = [False]*n
    answer=0
    
    def bfs(start):
        q = deque()
        q.append(start)
        visited[start] =True
        
        while q:
            now = q.popleft()
            
            for next_node in range(n):
                if computers[now][next_node]==1 and not visited[next_node]:
                    visited[next_node] = True
                    q.append(next_node)

    for i in range(n): # 0번부터 n-1번 컴퓨터까지 보면서 0번부터 n-1번 컴퓨터까지 보면서 새로운 네트워크 시작점이라는 뜻
        if not visited[i]:
            bfs(i)
            answer += 1               
    
    return answer
'''
def solution(n, computers):
    visited = [False] * n
    answer = 0

    def dfs(x):
        visited[x] = True

        for i in range(n):
            if computers[x][i] == 1 and not visited[i]:
                dfs(i)

    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1

    return answer