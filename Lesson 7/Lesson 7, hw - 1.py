class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        my_str = str()
        for el in self.matrix:
            n = ' '.join(map(str, el))
            my_str += n + '\n'
        return f'{my_str}'

    def __add__(self, other):
        result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(len(self.matrix)):
            for j in range(len(other.matrix[0])):
                result[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(result)


m1 = Matrix([[1, 5, 8], [5, 6, 3], [7, 9, 0]])
m2 = Matrix([[7, 1, 8], [2, 6, 8,], [3, 2, 9]])

print('Матрица №1')
print(m1)
print('Матрица №2')
print(m2)
print('Результат сложения матриц:')
print(m1 + m2)