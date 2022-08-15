from CheckField import CheckField
import numpy as np

SIZE = 9


class SolveField:
    def __init__(self, field):
        self.field = field
        self.max_set = {i + 1 for i in range(SIZE)}
        self.step_by_step = []

    def solve(self):
        while True:
            current_field = self.copy()
            self.field = self.last_possible(self.copy())
            self.field = self.last_hero(self.copy())
            if current_field == self.field:
                if CheckField(self.field).check():
                    return True
                return False

    @staticmethod
    def count_number(field, number):
        count, index = 0, []
        for i in range(SIZE):
            if len(str(field[i])) > 1:
                if number in field[i] and number not in field:
                    count += 1
                    index.append(i)
        return count, index

    def last_possible(self, field):
        transposed_field = self.transposing(self.copy())
        for i in range(SIZE):
            for j in range(SIZE):
                if not (len(str(field[i][j])) == 1 and field[i][j] != 0):
                    field[i][j] = list(self.max_set - {item for item in self.field[i] if len(str(item)) == 1} -
                                       {item for item in transposed_field[j] if len(str(item)) == 1} -
                                       {item for item in list(np.array(self.field, dtype=object)
                                        [i // 3 * 3:i // 3 * 3 + 3, j // 3 * 3:j // 3 * 3 + 3].reshape(9))
                                        if len(str(item)) == 1})
                    if len(field[i][j]) == 1:
                        field[i][j] = field[i][j][0]
                        self.step_by_step.append((field[i][j], i, j))
        return field

    def last_hero(self, field):
        for i in range(SIZE):
            for j in range(SIZE):
                field = self.last_hero_line(field, i, j)
                field = self.transposing(self.last_hero_col(self.transposing(field), i, j))
                field = self.last_hero_square(field, i, j)
        return field

    def last_hero_line(self, field, i, j):
        count, index = self.count_number(field[i], j + 1)
        if count == 1:
            field[i][index[0]] = j + 1
            self.step_by_step.append((j + 1, i, index[0]))
        return field

    def last_hero_col(self, field, i, j):
        count, index = self.count_number(field[i], j + 1)
        if count == 1:
            field[i][index[0]] = j + 1
            self.step_by_step.append((j + 1, index[0], i))
        return field

    def last_hero_square(self, field, i, j):
        if i % 3 == 0 and j % 3 == 0:
            for x in range(SIZE):
                count, index = self.count_number(list(np.array(field, dtype=object)
                                    [i // 3 * 3:i // 3 * 3 + 3, j // 3 * 3:j // 3 * 3 + 3].reshape(9)), x + 1)
                if count == 1:
                    field[i + index[0] // 3][j + index[0] % 3] = x + 1
                    self.step_by_step.append((x + 1, i + index[0] // 3, j + index[0] % 3))
        return field

    def copy(self):
        return [[self.field[i][j] for j in range(SIZE)] for i in range(SIZE)]

    def print_field(self, field):
        for item in field:
            print(item)

    def transposing(self, field):
        arr = []
        for i in range(SIZE):
            for j in range(SIZE):
                if (j, i) not in arr:
                    arr.append((i, j))
                    field[i][j], field[j][i] = field[j][i], field[i][j]
        return field
