import numpy as np
SIZE = 9


class SolveField:
    def __init__(self, field):
        self.field = field
        self.max_set = {i + 1 for i in range(SIZE)}
        self.transposed_field = np.array(field).T
        self.solve()
        self.print_field()

    def solve(self):
        while True:
            current_field = self.copy()
            self.field = self.solve_one_step(self.copy())
            if current_field == self.field:
                break

    def solve_one_step(self, field):
        for i in range(SIZE):
            row = set(self.field[i])
            for j in range(SIZE):
                if type(field[i][j]) == int and field[i][j] != 0:
                    field[i][j] = [self.field[i][j]]
                else:
                    field[i][j] = list(self.max_set - row - set(self.transposed_field[j]) -
                                       set(np.array(self.field)[i//3*3:i//3*3 + 3, j//3*3:j//3*3 + 3].reshape(9)))
        return field

    def copy(self):
        arr = []
        for i in range(SIZE):
            arr.append([self.field[i][j] for j in range(SIZE)])
        return arr

    def print_field(self):
        for item in self.field:
            print(item)
