import time


def read_puzzle():
    b = ""
    banks = []
    with open("input.txt", "r") as f:
        b = f.read()
    banks = b.split("\n")
    banks.remove("")
    return banks


def solve_pt1(banks: list[str]) -> int:
    solution = 0

    for bank in banks:
        jolts = 0
        cells: list[int] = []

        for i in range(len(bank)):
            cells.append(int(bank[i]))

        jolts_tens = max(cells[:-1])
        jolts_tens_index = cells.index(jolts_tens)

        jolts_ones = max(cells[jolts_tens_index + 1 :])

        jolts = jolts_tens * 10
        jolts += jolts_ones
        solution += jolts
    return solution


def solve_pt2(banks: list[str]) -> int:
    solution = 0

    for bank in banks:
        index = 0
        jolts = 0
        cells: list[str] = []

        magic_num = 12

        for i in range(len(bank)):
            cells.append(bank[i])
        cells.extend(["0"])
        cell_jolts = []
        for i in range(0, magic_num):
            maximum = max(cells[index : (i - magic_num)])

            index = cells.index(maximum, index, (i - magic_num))

            cells[index] = "0"

            cell_jolts.append(maximum)

        jolts = int("".join(cell_jolts))
        solution += jolts

    return solution


if __name__ == "__main__":
    puzzle = read_puzzle()

    t_pt1_start = time.time()
    solution_pt1 = solve_pt1(puzzle)
    t_pt1_end = time.time()
    pt1_total = t_pt1_end - t_pt1_start

    t_pt2_start = time.time()
    solution_pt2 = solve_pt2(puzzle)
    t_pt2_end = time.time()
    pt2_total = t_pt2_end - t_pt2_start

    print(f"solution to pt1 is {solution_pt1}, took: {pt1_total:.3f} seconds")
    print(f"solution to pt2 is {solution_pt2}, took: {pt2_total:.3f} seconds")
