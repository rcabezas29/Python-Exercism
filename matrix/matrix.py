class Matrix:
    def __init__(self, matrix_string):
        self.matrix = []
        rows = matrix_string.split("\n")
        for a in rows:
            self.matrix.append(a.split(" "))

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        column = []
        for row in self.matrix:
            column.append(row[index - 1])
        return column