from CheckField import CheckField

SIZE = 9
all_field = [[5, 2, 1, 9, 7, 3, 6, 4, 8],
             [4, 9, 3, 6, 8, 5, 7, 2, 1],
             [7, 8, 6, 1, 2, 4, 5, 3, 9],
             [9, 7, 5, 2, 4, 8, 1, 6, 3],
             [6, 1, 4, 7, 3, 9, 2, 8, 5],
             [2, 3, 8, 5, 1, 6, 4, 9, 7],
             [1, 6, 2, 3, 9, 7, 8, 5, 4],
             [3, 4, 7, 8, 5, 2, 9, 1, 6],
             [8, 5, 9, 4, 6, 1, 3, 7, 2]]


def main():
    checker = CheckField(all_field)
    print(checker.response())


if __name__ == "__main__":
    main()
