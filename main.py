# from CheckField import CheckField
from SolveField import SolveField

SIZE = 9
sudoku = [[0, 0, 7, 1, 2, 0, 5, 0, 8],
          [4, 2, 0, 8, 5, 0, 3, 9, 0],
          [1, 5, 8, 0, 4, 9, 2, 0, 0],
          [0, 7, 3, 6, 0, 4, 0, 1, 0],
          [8, 4, 0, 9, 1, 3, 0, 0, 7],
          [9, 6, 0, 0, 0, 2, 8, 3, 4],
          [5, 0, 4, 0, 9, 1, 0, 6, 0],
          [0, 0, 2, 4, 6, 5, 0, 8, 0],
          [6, 1, 9, 7, 0, 0, 4, 0, 0]]


def main():
    # checker = CheckField(all_field)
    # SolveField(sudoku)
    print(set([1, 2, 3, [4], 5]))
    # print(checker.response())
    # solver.print_field()


if __name__ == "__main__":
    main()
