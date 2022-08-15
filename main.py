from SolveField import SolveField
from GraphicsDesign import graphics_main
from GlobalValues import sudoku


def print_field(field):
    for item in field:
        print(item)


def main():
    solver = SolveField(sudoku.copy())
    if solver.solve():
        print_field(solver.field)
        graphics_main(solver.field)
    else:
        print(sudoku)
        print('Too hard for me now')
        graphics_main(solver.field)
        print_field(solver.field)


if __name__ == "__main__":
    main()
