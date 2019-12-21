"""
Sudoku parser and solver

This module creates a command-line sudoku solver. The input is expected to be
a sudoku puzzle with whitespace and 0's to represent empty positions. One
puzzle per line. Output is the solution, if it exists, or a blank line if no
solution exists.

For example here is an example of one puzzle on a single line and the solution.

```
$ echo "008342900009000700400000003006473200030000010002851600700000008004000100003697500" | python -m sudoku.solve
678342951329185764451769823516473289837926415942851637765214398294538176183697542
```

Above is just the below puzzle without any whitespace.

[[0, 0, 8, 3, 4, 2, 9, 0, 0],
 [0, 0, 9, 0, 0, 0, 7, 0, 0],
 [4, 0, 0, 0, 0, 0, 0, 0, 3],
 [0, 0, 6, 4, 7, 3, 2, 0, 0],
 [0, 3, 0, 0, 0, 0, 0, 1, 0],
 [0, 0, 2, 8, 5, 1, 6, 0, 0],
 [7, 0, 0, 0, 0, 0, 0, 0, 8],
 [0, 0, 4, 0, 0, 0, 1, 0, 0],
 [0, 0, 3, 6, 9, 7, 5, 0, 0]]
"""
import fileinput
from itertools import chain
from sudoku.solver import solve


def read(line):
    """
    >>> parse('008342900009000700400000003006473200030000010002851600700000008004000100003697500')
    [[0, 0, 8, 3, 4, 2, 9, 0, 0], [0, 0, 9, 0, 0, 0, 7, 0, 0], [4, 0, 0, 0, 0, 0, 0, 0, 3], [0, 0, 6, 4, 7, 3, 2, 0, 0], [0, 3, 0, 0, 0, 0, 0, 1, 0], [0, 0, 2, 8, 5, 1, 6, 0, 0], [7, 0, 0, 0, 0, 0, 0, 0, 8], [0, 0, 4, 0, 0, 0, 1, 0, 0], [0, 0, 3, 6, 9, 7, 5, 0, 0]]
    """
    return [[int(v) for v in  line[i*9:i*9+9]] for i in range(9)]


def write(board):
    """
    >>> format([
    ... [0, 0, 8, 3, 4, 2, 9, 0, 0],
    ... [0, 0, 9, 0, 0, 0, 7, 0, 0],
    ... [4, 0, 0, 0, 0, 0, 0, 0, 3],
    ... [0, 0, 6, 4, 7, 3, 2, 0, 0],
    ... [0, 3, 0, 0, 0, 0, 0, 1, 0],
    ... [0, 0, 2, 8, 5, 1, 6, 0, 0],
    ... [7, 0, 0, 0, 0, 0, 0, 0, 8],
    ... [0, 0, 4, 0, 0, 0, 1, 0, 0],
    ... [0, 0, 3, 6, 9, 7, 5, 0, 0]
    ... ])
    '008342900009000700400000003006473200030000010002851600700000008004000100003697500'
    """
    return ''.join([str(c) for c in chain(*board)])


if __name__ == '__main__':
    for line in fileinput.input():
        print(write(solve(read(line))))
