from collections import deque

n = int(input())
maps = [list(input()) for _ in range(n)]
dx = [1, -1, 0, 0]    # 오, 왼, 위, 아
dy = [0, 0, 1, -1]
que = deque()

num = []
count_hs = 0               # 단지의 개수
for i in range(n):
    for j in range(n):
        if maps[i][j] == '1':
            count_hs += 1
            count = 1                 # 각 단지의 집의 개수
            maps[i][j] = 0
            que.append((i, j))
            while que:
                a, b = que.popleft()
                for k in range(4):
                    x = a + dx[k]
                    y = b + dy[k]
                    if  0 <= x < n and 0 <= y < n and maps[x][y] == '1':
                        count += 1
                        que.append((x,y))
                        maps[x][y] = 0
            num.append(count)
print(count_hs)
num.sort()
for i in range(len(num)):
    print(num[i])
