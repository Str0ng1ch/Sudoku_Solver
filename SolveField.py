from CheckField import CheckField
import numpy as np

SIZE = 9


class SolveField:
    def __init__(self, field):
        self.field = field
        self.start_field = self.copy()
        self.max_set = {i + 1 for i in range(SIZE)}
        self.step_by_step = []
        self.solve()

    def solve(self):
        while True:
            current_field = self.copy()
            self.transposed_field = np.array(self.field, dtype=object).T
            self.field = self.last_possible(self.copy())
            if current_field == self.field:
                if CheckField(self.field).check:
                    return True
                return False

    def last_possible(self, field):
        for i in range(SIZE):
            for j in range(SIZE):
                if not (len(str(field[i][j])) == 1 and field[i][j] != 0):
                    field[i][j] = list(self.max_set - {item for item in self.field[i] if len(str(item)) == 1} -
                                       {item for item in self.transposed_field[j] if len(str(item)) == 1} -
                                       {item for item in list(np.array(self.field, dtype=object)
                                        [i // 3 * 3:i // 3 * 3 + 3, j // 3 * 3:j // 3 * 3 + 3].reshape(9))
                                        if len(str(item)) == 1})
                    if len(field[i][j]) == 1:
                        field[i][j] = field[i][j][0]
                        self.step_by_step.append((field[i][j], i, j))
        return field

    def copy(self):
        return [[self.field[i][j] for j in range(SIZE)] for i in range(SIZE)]
