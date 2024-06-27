class Matrix:
    def __init__(self, grid=None):
        if grid is None:
            grid = []
            self.l = 0
        else:
            self.g = grid
            self.l = len(grid[0])

    def __len__(self):
        return len(self.l)

    def __getitem__(self, idx):
        return self.g[idx]

    def __setitem__(self, idx, item):
        self.g[idx] = item

    def __str__(self):
        return "\n" + "\n".join([str(i) for i in [rows for rows in self.g]]) + "\n"

    def __mul__(self, other):
        result = [[sum(a * b for a, b in zip(self_row, other_col)) for other_col in zip(*other.g)] for self_row in
                  self.g]
        return Matrix(result)

import random
def fill_square_matrix(size):
    matrix = []
    matrix = [[random.randint(0, 9) for i in range(size)] for i in range(size)]
    return matrix




      

matrix1 = Matrix()
matrix2 = Matrix()

n = int(input('n = '))
while n < 1:
    n = int(input('n = '))
matrix1 = Matrix(fill_square_matrix(n))
print('    Матриця 1         ')
print(matrix1)

matrix2 = Matrix(fill_square_matrix(n))
print('    Матриця 2         ')
print(matrix2)

result = matrix1 * matrix2
print('    Результат множення матриці 1 на матрицю 2 ')
print(result)


