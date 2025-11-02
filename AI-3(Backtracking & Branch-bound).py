# Backtracking
def is_safe(board, r, c, n):
    for i in range(c):
        if board[r][i] or (r-i-1 >= 0 and c-i-1 >= 0 and board[r-i-1][c-i-1]) \
           or (r+i+1 < n and c-i-1 >= 0 and board[r+i+1][c-i-1]):
            return False
    return True

def solve_bt(board, c, n):
    if c == n: return True
    for r in range(n):
        if is_safe(board, r, c, n):
            board[r][c] = 1
            if solve_bt(board, c+1, n): return True
            board[r][c] = 0
    return False

# Branch & Bound
def solve_bb(n):
    col, ld, rd = [0]*n, [0]*(2*n), [0]*(2*n)
    board = [[0]*n for _ in range(n)]
    def solve(c):
        if c == n: return True
        for r in range(n):
            if not col[r] and not ld[r-c] and not rd[r+c]:
                board[r][c] = col[r] = ld[r-c] = rd[r+c] = 1
                if solve(c+1): return True
                board[r][c] = col[r] = ld[r-c] = rd[r+c] = 0
        return False
    solve(0)
    return board

# Run Example
n = 4
board1 = [[0]*n for _ in range(n)]
solve_bt(board1, 0, n)
print("Backtracking:")
for r in board1: print(r)

board2 = solve_bb(n)
print("\nBranch & Bound:")
for r in board2: print(r)
