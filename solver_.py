from sudoku_ import Sudoku_s

class SudokuSolver_s:
    def __init__(self, sudoku: Sudoku_s):
        self._s = sudoku

    @property
    def overall_unknown(self):
        count = 0
        for row in self._s.puzzel:
            for s in row:
                if s == 0:
                    count += 1
        return count
        
    @property
    def solved(self):
        return self.overall_unknown == 0
                                                                          
    def _solve_easy(self):
        has_1 = 0
        for row in self._s.rows_p:
            for s_ in row:
                val = self._s[s_]
                if not val:
                    a = self._s.can_use_s_(s_)
                    if a:
                        if len(a) == 1:
                            has_1 += 1
                            self._s[s_] = a.pop()
        if has_1 >= 1:
            return True
        return False
        
    def full_solve(self):
        while True:
            if not self._solve_easy():
                return None
            
            if self.solved:
                return self._s
    
