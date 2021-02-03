# 1 Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
# __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде
# прямоугольной схемы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
# привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
# объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
# строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, matrix_list_1):
        self.list_1 = matrix_list_1
        # Размер итоговой матрицы должен совпадать с размером входной матрицы
        self.__add_matrix = matrix_list_1

    def __str__(self):
        return str('-- Исходная матрица --\n' + '\n'.join(['\t'.join([str(j) for j in i]) for i in self.list_1]))

    def count_list(self, u_list):
        count = 0
        for i in range(len(u_list)):
            count += len(u_list[i])
        return count

    def __add__(self, other):
        if self.count_list(self.list_1) != self.count_list(other.list_1):
            return 'Неверный размер матриц'
        try:
            for i in range(len(self.list_1)):
                for j in range(len(other.list_1[i])):
                    self.__add_matrix[i][j] = self.list_1[i][j] + other.list_1[i][j]
            return str('-- Итоговая матрица --\n' + '\n'.join(['\t'.join([str(j) for j in i]) for i in self.__add_matrix]))
        except IndexError:
            return 'Индекс за пределами массива'


matrix = Matrix([[1, 4, 8, 9], [11, 14, 18, 9], [21, 26, 31, 9]])
matrix2 = Matrix([[70, 3, 19, 7], [80, 1, 15, 7], [42, 9, 3, 7]])
print(matrix)
print(matrix2)
print(matrix + matrix2)
