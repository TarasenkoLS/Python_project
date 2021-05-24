class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join("   ".join([f"{i:3}" for i in line]) for line in self.matrix)

    def __add__(self, other):
        num_str = len(self.matrix)
        num_col = len(self.matrix[0])
        result = []
        try:
            for i in range(num_str):
                for j in range(num_col):
                    self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
                result = self.matrix
            return Matrix(result)
        except IndexError:
            return f"Ошибка! Матрицы имеют разную размерность!"



matrix_1 = Matrix([[7, 16], [12, 4], [15, 26]])
matrix_2 = Matrix([[8, 5], [4, 3], [1, 6]])

print(f"{matrix_1}")
print(matrix_1 + matrix_2)
