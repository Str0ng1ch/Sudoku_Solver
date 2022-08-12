import numpy as np

SIZE = 9


class CheckField:
    def __init__(self, field):
        self.field = field
        self.transposed_field = np.array(field, dtype=object).T

    def check(self):
        for i in range(SIZE):
            if 0 in self.field[i] or self.check_line(i) or self.check_square(i):
                return False
        return True

    def check_line(self, i):
        return (len({item for item in self.field[i] if len(str(item)) == 1}) != SIZE or
                len({item for item in self.transposed_field[i] if len(str(item)) == 1}) != SIZE)

    def check_square(self, i):
        return False if i % 3 != 0 else (list(len({item for item in list(np.array(self.field, dtype=object)
                                        [i // 3 * 3:i // 3 * 3 + 3, j:j + 3].reshape(9)) if len(str(item)) == 1})
                                        for j in range(0, 3)) != [SIZE, SIZE, SIZE])
