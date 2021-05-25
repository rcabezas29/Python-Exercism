class Matrix:
    def __init__(self, matrix_string):
        self.matrix = []
        self.matrix = [[int(n) for n in line.split()] for line in matrix_string.splitlines()]

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [column[index - 1] for column in self.matrix]
