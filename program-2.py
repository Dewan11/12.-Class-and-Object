class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix  

    def show(self):
        for row in self.matrix:
            print(row)
            
    def add(self, b):
        return Matrix([[self.matrix[i][j] + b.matrix[i][j] for j in range(3)] for i in range(3)])

    def mul(self, b):
        return Matrix([[sum(self.matrix[i][k] * b.matrix[k][j] for k in range(3)) for j in range(3)] for i in range(3)])

    def trans(self):
        return Matrix([[self.matrix[j][i] for j in range(3)] for i in range(3)])


# Example usage
a = Matrix([[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]])

b = Matrix([[9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]])

print("A + B:")
a.add(b).show()

print("\nA * B:")
a.mul(b).show()

print("\nTranspose of A:")
a.trans().show()
