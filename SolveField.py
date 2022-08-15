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
            self.transposed_field = np.array(self.field, dtype=object).T
            self.last_possible()
            # self.transposed_field = np.array(self.field, dtype=object).T
            # self.field = self.last_hero_row(self.copy())
            self.transposed_field = np.array(self.field, dtype=object).T
            self.last_hero_col()
            if current_field == self.field:
                print(self.step_by_step)
                if CheckField(self.field).check():
                    return True
                return False

    @staticmethod
    def count_number(field, number):
        count, index = 0, []
        for i in range(SIZE):
            if len(str(field[i])) > 1:
                if number in field[i]:
                    count += 1
                    index.append(i)
        return count, index

    def last_possible(self):
        for i in range(SIZE):
            for j in range(SIZE):
                if not (len(str(self.field[i][j])) == 1 and self.field[i][j] != 0):
                    self.field[i][j] = list(self.max_set - {item for item in self.field[i] if len(str(item)) == 1} -
                                       {item for item in self.transposed_field[j] if len(str(item)) == 1} -
                                       {item for item in list(np.array(self.field, dtype=object)
                                        [i // 3 * 3:i // 3 * 3 + 3, j // 3 * 3:j // 3 * 3 + 3].reshape(9))
                                        if len(str(item)) == 1})
                    if len(self.field[i][j]) == 1:
                        self.field[i][j] = self.field[i][j][0]
                        self.transposed_field = np.array(self.field, dtype=object).T
                        self.step_by_step.append((self.field[i][j], i, j))

    def last_hero_row(self, field):
        for i in range(SIZE):
            for j in range(SIZE):
                count, index = self.count_number(self.field[i], j + 1)
                if count == 1:
                    field[i][index[0]] = j + 1
                    self.step_by_step.append((j + 1, i, index[0]))
        return field

    def last_hero_col(self):
        for i in range(SIZE):
            for j in range(SIZE):
                count, index = self.count_number(self.transposed_field[i], j + 1)
                if count == 1:
                    self.field[index[0]][i] = j + 1
                    self.transposed_field = np.array(self.field, dtype=object).T
                    self.step_by_step.append((j + 1, index[0], i))
                # if i % 3 == 0 and j % 3 == 0:
                #     for x in range(SIZE):
                #         count, index = self.count_number(list(np.array(self.field, dtype=object)
                #                             [i // 3 * 3:i // 3 * 3 + 3, j // 3 * 3:j // 3 * 3 + 3].reshape(9)), x + 1)
                #         if count == 1:
                #             field[i + index[0] // 3][j + index[0] % 3] = x + 1
                #             self.step_by_step.append((x + 1, i + index[0] // 3, j + index[0] % 3))

    def copy(self):
        return [[self.field[i][j] for j in range(SIZE)] for i in range(SIZE)]
