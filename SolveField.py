from CheckField import CheckField
import numpy as np

SIZE = 9


class SolveField:
    def __init__(self, field):
        self.field = field
        self.max_set = {i + 1 for i in range(SIZE)}

    def solve(self):
        while True:
            current_field = self.copy()
            self.transposed_field = np.array(self.field, dtype=object).T
            self.field = self.solve_one_step(self.copy())
            if current_field == self.field:
                if CheckField(self.field).check:
                    return True
                return False

    def solve_one_step(self, field):
        for i in range(SIZE):
            for j in range(SIZE):
                if not (type(field[i][j]) == int and field[i][j] != 0):
                    field[i][j] = list(self.max_set - set(item for item in self.field[i] if type(item) == int) - set(
                        item for item in self.transposed_field[j] if
                        (type(item) == np.int32 or type(item) == int)) - set(item for item in
                        list(np.array(self.field, dtype=object)
                             [i // 3 * 3:i // 3 * 3 + 3, j // 3 * 3:j // 3 * 3 + 3].reshape(9)) if type(item) == int))
                    field[i][j] = field[i][j][0] if len(field[i][j]) == 1 else field[i][j]
        return field

    def copy(self):
        arr = []
        for i in range(SIZE):
            arr.append([self.field[i][j] for j in range(SIZE)])
        return arr
