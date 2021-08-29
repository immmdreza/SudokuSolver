# SudokuSolver
A sudoku solver written in python ( Easy sudoku for now )

### What's easy sudoku 
An easy sudoku has at least one unkown Square which has only one possible value in every solving process. till no unknown square remains.

```py

from sudoku_ import Sudoku_s
from solver_ import SudokuSolver_s

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

sudoku_s = Sudoku_s(puzzle)
solver_s = SudokuSolver_s(sudoku_s)

if solver_s.full_solve():
    print(sudoku_s)

```

An answer to [Kata](https://www.codewars.com/kata/5296bc77afba8baa690002d7/)
