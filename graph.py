class Matrix:
    def __init__(self, size):
        self.size = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)] 

    def create_greaph(self, edges=[]):
        for i,j in edges:
            self.graph[i][j] = 1
            self.graph[j][i] = 1

    def __str__(self):
        s = ""
        for i in range(1, self.size):
            s += "\n"
            for j in range(1, self.size):
                s += str(self.graph[i][j]) + " "
        return s        



matrix = Matrix(5)

edges = [(1,2),(2,3),(3,4),(4,2),(1,3)]
matrix.create_greaph(edges)

print(matrix)    