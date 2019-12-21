"""
Sudoku Solver

Board is a 9x9 game board. `solve()` returns a solution of None, if none exist.
"""
from itertools import product
from copy import deepcopy


ALL_NUMS = {v for v in range(1,10)}

def region_values(board, row, col):
    return {v for r, c in product(range(3), range(3)) if (v := board[row+r][col+c])}

def col_values(board, col):
    return {v for r in range(9) if (v := board[r][col])}

def row_values(board, row):
    return {v for c in range(9) if (v := board[row][c])}

def valid_values(board, row, col):
    row_vals = row_values(board, row)
    col_vals = col_values(board, col)
    region_vals = region_values(board, row // 3 * 3, col // 3 * 3)
    return ALL_NUMS - (row_vals | col_vals | region_vals)

def valid_solution(board):
    valid_rows = all([ALL_NUMS == row_values(board, r) for r in range(9)])
    valid_cols = all([ALL_NUMS == col_values(board, c) for c in range(9)])
    valid_regions = all([ALL_NUMS == region_values(board, r*3, c*3) for r, c in product(range(3), range(3))])
    return valid_rows and valid_cols and valid_regions

def solve(board):
    if valid_solution(board):
        return board
    solutions = [(v, row, col) for row, col in product(range(9), range(9)) if not board[row][col] if (v := valid_values(board, row, col))]
    one_solutions = [solution for solution in solutions if len(solution[0]) == 1]
    if one_solutions:
        # unambiguous moves can be done all at once, no copy of board needed
        for (v, *_), r, c in one_solutions:
            board[r][c] = v
        return solve(board)
    else:
        # try all combos, starting with fewest possibilities first
        for vals, r, c in sorted(solutions, key=lambda k: len(k[0])):
            for val in vals:
                next_board = deepcopy(board)
                next_board[r][c] = val
                if solution := solve(next_board):
                    return solution
