from SolveField import SolveField

SIZE = 9
sudoku = [[0, 7, 0, 1, 0, 0, 9, 0, 0],
          [0, 0, 1, 0, 0, 6, 0, 0, 4],
          [9, 0, 8, 2, 4, 0, 1, 7, 0],
          [0, 9, 0, 0, 0, 0, 5, 0, 6],
          [0, 0, 5, 0, 0, 0, 7, 0, 0],
          [8, 0, 7, 0, 0, 0, 0, 3, 0],
          [0, 8, 3, 0, 7, 2, 6, 0, 5],
          [2, 0, 0, 5, 0, 0, 4, 0, 0],
          [0, 0, 6, 0, 0, 4, 0, 2, 0]]


def print_field(field):
    for item in field:
        print(item)


def main():
    solver = SolveField(sudoku)
    if solver.solve():
        print_field(solver.field)
    else:
        print('Too hard for me now')
        print_field(solver.field)


if __name__ == "__main__":
    main()
