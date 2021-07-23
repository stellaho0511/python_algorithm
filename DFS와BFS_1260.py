from collections import deque

def dfs(start):
    visited[start] = 1
    print(start, end = ' ')
    for i in range(1, n+1):
        if visited[i] == 0 and graph[start][i] == 1:
            dfs(i)

def bfs(start):
    queue = deque([start])
    visited[start] = 0
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in range(1, n+1):
            if visited[i] == 1 and graph[v][i] == 1:
                queue.append(i)
                visited[i] = 0

n, m, v = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

visited = [0] * (n+1)
dfs(v)
print()
bfs(v)
