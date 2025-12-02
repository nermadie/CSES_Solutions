def mark_attacked(board, row, col):
    for i in range(row, 8):
        board[i][col] = "*"
        if col + (i - row) < 8:
            board[i][col + (i - row)] = "*"
        if col - (i - row) >= 0:
            board[i][col - (i - row)] = "*"


def solve(board):
    result = 0
    save_stack = []
    for i in range(8):
        if board[0][i] == ".":
            board_temp = [row[:] for row in board]
            mark_attacked(board_temp, 0, i)
            row = 1
            col = i
            save_stack.append((board_temp, row, col))

    while len(save_stack) > 0:
        board_curr, row, col = save_stack.pop()
        if row == 8:
            result += 1
            continue
        for j in range(8):
            if board_curr[row][j] == ".":
                board_temp = [r[:] for r in board_curr]
                mark_attacked(board_temp, row, j)
                save_stack.append((board_temp, row + 1, j))

    return result


board = []
for i in range(8):
    board.append(list(input().strip()))
print(solve(board))
