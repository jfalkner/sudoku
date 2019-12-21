# Sudoku solver and generator

This is a Python-based Sudoku game solver and generator. Check out [wikipedia's Sudoku page](https://en.wikipedia.org/wiki/Sudoku) if you are unfamiliar with the game.

## Command-line Example

Boards can be solved by passing them in one line at time as shown below (python 3.8+ is required). 

```
echo "008342900009000700400000003006473200030000010002851600700000008004000100003697500" | python -m sudoku.solve
678342951329185764451769823516473289837926415942851637765214398294538176183697542
```

Output is the solved board. It currently takes a fraction of a second to solve a puzzle.

If the above board is confusing, see [sudoku/solve.py](sudoku/solve.py) for it displayed in a 9x9 format.

## Python API Example

Boards are internally worked with as a 9x9 array. Pass such an array to `solve()` to get the solution or `None`, if no solution exists

```
from sudoku.solver import solve

solution =  solve([
    [0, 0, 4, 0, 0, 0, 5, 0, 0],
    [0, 7, 0, 2, 0, 0, 3, 6, 0],
    [8, 0, 0, 0, 0, 1, 0, 0, 0],
    [6, 2, 9, 0, 0, 0, 0, 3, 0],
    [0, 0, 0, 0, 6, 0, 0, 0, 0],
    [0, 4, 0, 0, 0, 0, 6, 1, 8],
    [0, 0, 0, 7, 0, 0, 0, 0, 6],
    [0, 1, 3, 0, 0, 4, 0, 2, 0],
    [0, 0, 2, 0, 0, 0, 4, 0, 0]
])
```

If formatting to match the CLI example is desired, see the `read` and `write` methods in [sudoku/solve.py](sudoku/solve.py).


