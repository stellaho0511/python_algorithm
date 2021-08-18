# 웜 바이러스
def dfs(v):
    global cnt
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            dfs(i)

def bfs(v):
    global cnt
    que = [v]
    while que:
        n = que.pop(0)

        


n = int(input())         # 컴퓨터 수
l = int(input())         # 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수
graph = [[] for i in range(n+1)]

for i in range(l):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
cnt = 0
dfs(1)
print(cnt)
