import numpy as np
SIZE = 9


class CheckField:
    def __init__(self, field):
        self.field = field
        self.transposed_field = np.array(field, dtype=object).T
        self.check = self.check_line() * self.check_square()

    def check_line(self):
        for i in range(SIZE):
            if (len(set(item for item in self.field[i] if type(item) == int)) != SIZE or 0 in self.field[i] or
                    len(set(item for item in self.transposed_field[i] if type(item) == np.int32)) != SIZE):
                return False
        return True

    def check_square(self):
        for i in range(0, SIZE, 3):
            for j in range(0, SIZE, 3):
                if len(set(item for item in list(np.array(self.field, dtype=object)
                    [i // 3 * 3:i // 3 * 3 + 3, j // 3 * 3:j // 3 * 3 + 3].reshape(9)) if type(item) == int)) != SIZE:
                    return False
        return True
