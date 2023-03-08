class Matrix:
    def __init__(self, rows, cols, data):
        self.rows = rows
        self.cols = cols
        if data is None:
            self.data = [[0 for i in range(rows)] for j in range(cols)]
        else:
            self.data = data

    def __str__(self):
        matrix_str = ""
        for row in range(self.rows):
            matrix_str += "|"
            for col in range(self.cols):
                matrix_str += f"{self.data[row][col]:6.2f}"
            matrix_str += " |\n"
        return matrix_str

    def copy(self):
        n = self.rows
        c = Matrix(n, n, None)
        for i in range(n):
            for j in range(n):
                c.data[i][j] = self.data[i][j]
        return c

    def det(self):
        n = self.rows

        if n == 1:
            return self.data[0][0]

        if n == 2:
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]

        det_A = 0
        for j in range(n):
            submatrix = [row[:j] + row[j + 1:] for row in self.data[1:]]
            det_A += (-1) ** j * self.data[0][j] * Matrix(n - 1, n - 1, submatrix).det()

        return det_A

    def dot(A, B):
        if len(A.cols) != len(B.rows):
            raise ValueError(
                "Number of columns in the first matrix must match the number of rows in the second matrix.")
        c = [[0 for j in range(B.cols)] for i in range(A.rows)]
        C = Matrix(A.rows, B.cols, c)
        for i in range(A.rows):
            for j in range(A.cols):
                for k in range(B.cols):
                    C.data[i][j] += A.data[i][k] * B.data[k][j]
        return C