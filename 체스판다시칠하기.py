n, m = map(int, input().split())
board = list()
for i in range(n):
    board.append(input())
repair = list()
for i in range(n-7):
    for j in range(m-7):
        w = 0
        b = 0
        for c in range(i, i + 8):
            for r in range(j, j+8):
                k = board[c][r]
                if (r + c) % 2 == 0:
                    if k != 'W':
                        w += 1
                    else:
                        b += 1
                else:
                    if k != 'B':
                        w += 1
                    else:
                        b += 1
        repair.append(min(w, b))
print(min(repair))
