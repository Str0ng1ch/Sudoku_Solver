from SolveField import SolveField
from GraphicsDesign import graphics_main
from GlobalValues import sudoku

solver = SolveField(sudoku)


def print_field(field):
    for item in field:
        print(item)


def main():
    if solver.solve():
        print_field(solver.field)
        graphics_main(solver.field)
    else:
        print('Too hard for me now')
        print_field(solver.field)


if __name__ == "__main__":
    main()
