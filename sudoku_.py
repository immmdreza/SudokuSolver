from typing import List, Tuple

class Sudoku_s:
    def __init__(self, your_sudoku: List[List[int]]):
        self._p = your_sudoku
        self._f = set(self.fixed_s_())
    
    @property    
    def puzzel(self):
        return self._p
    
    @property    
    def fixed_p(self):
        return self._f
           
    @property   
    def rows_p(self) -> List[List[Tuple[int, int]]]:
        for row in range(9):
            yield [(row, s) for s in range(9)]
          
    @property  
    def cols_p(self) -> List[List[Tuple[int, int]]]:
        for col in range(9):
            yield [(s, col) for s in range(9)]
    
    @property
    def blks_p(self) -> List[List[Tuple[int, int]]]:
        for x_line in range(3):
            x_seed = x_line*3
            for y_line in range(3):
                y_seed = y_line*3
                block = []
                for x in range(x_seed, x_seed + 3):
                    for y in range(y_seed, y_seed + 3):
                        block.append((x, y))
                yield block
                
    def fixed_s_(self):
        for i, r in enumerate(self._p):
            for j, s in enumerate(r):
                if s:
                    yield (i, j)
                
    def get_s_item(self, p: Tuple[int, int]):
        return self._p[p[0]][p[1]]
        
    def set_s_item(self, p: Tuple[int, int], val: int):
        self._p[p[0]][p[1]] = val
        
    def get_row(self, tpl):
        return next(filter(lambda x: tpl in x, self.rows_p))
        
    def get_col(self, tpl):
        return next(filter(lambda x: tpl in x, self.cols_p))
    
    def get_blk(self, tpl):
        return next(filter(lambda x: tpl in x, self.blks_p))
        
    def used(self, c):
        return set(filter(lambda x: x,[self[s_] for s_ in c]))
        
    def not_used(self, c):
        return set(range(1, 10)) - self.used(c)
    
    def can_use_s_(self, tpl):
        row = self.get_row(tpl)
        n_r = self.not_used(row)
        column = self.get_col(tpl)
        n_t = self.not_used(column)
        block = self.get_blk(tpl)
        n_b = self.not_used(block)
    
        return ( n_r & n_t ) & n_b
    
    def row_at(self, index: int):
        for i, x in enumerate(self.rows_p):
            if i == index:
                return x
                
    def col_at(self, index: int):
        for i, x in enumerate(self.cols_p):
            if i == index:
                return x
                
    def blk_at(self, index: int):
        for i, x in enumerate(self.blks_p):
            if i == index:
                return x
        
    def __getitem__(self, p):
        return self.get_s_item(p)
        
    def __setitem__(self, p, val):
        self.set_s_item(p, val)
        
    def blk_str(self, index: int):
        s = ''
        for i, x in enumerate(self.blk_at(index)):
            s += f'[{self[x]}]'
            if (i + 1) % 3 == 0:
                s += '\n'
        return s
        
    def __str__(self):
        s = ' '
        for j, r in enumerate(self.rows_p):
            for i, p in enumerate(r):
                s += f'[{self[p]}]'
                if (i + 1) % 3 == 0:
                    if i + 1 != 9:
                        s += ' | '
            if (j + 1) % 3 == 0:
                s += '\n' + ' _ '*12 + '\n\n '
            else:
                s += '\n '
        return s
        
    def iter_c(self, c: List[Tuple[int, int]]):
        for p in c:
            yield self.get_s_item(p)
            
