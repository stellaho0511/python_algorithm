n, m = map(int, input().split())
board = []
dx = [1, -1, 0, 0]   # 좌, 우, 상, 하
dy = [0, 0, 1, -1]
for _ in range(n):
    board.append(list(input()))
que = [[0,0]]
board[0][0] = 1
while que:
    nx, ny = que.pop(0)
    for i in range(4):
        x = nx + dx[i]
        y = ny + dy[i]
        if 0 <= x < n and 0 <= y < m and board[x][y] == '1':
            que.append([x,y])
            board[x][y] = board[nx][ny] + 1
print(board[n-1][m-1])
