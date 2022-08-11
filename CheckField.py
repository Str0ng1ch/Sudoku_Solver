import numpy as np
SIZE = 9


class CheckField:
    def __init__(self, field):
        self.field = field
        self.transposed_field = np.array(field).T
        self.check = self.check_line() * self.check_square()

    def check_line(self):
        for i in range(SIZE):
            if (len(set(self.field[i])) != SIZE or 0 in self.field[i] or
                    len(set(self.transposed_field[i])) != SIZE):
                return False
        return True

    def check_square(self):
        for i in range(0, SIZE, 3):
            for j in range(0, SIZE, 3):
                if len(set(np.array(self.field)[i:i + 3, j:j + 3].reshape(9))) != SIZE:
                    return False
        return True
