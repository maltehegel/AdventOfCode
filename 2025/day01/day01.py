import time

start_position = 50
mod = 100


def read_puzzle() -> list[int]:
    input = []
    ints = []
    with open("input.txt", "r") as file:
        input = file.read().splitlines()

    for line in input:
        if line[0] == "R":
            ints.append(int(line[1:]))
        elif line[0] == "L":
            ints.append(-int(line[1:]))
        else:
            continue
    return ints


def solve_pt1(puzzle: list[int]) -> int:
    pwd = 0
    current_position = start_position

    for i in puzzle:
        current_position += i
        current_position = current_position % mod
        if current_position == 0:
            pwd += 1

    return pwd


def solve_pt2(puzzle: list[int]) -> int:
    pwd = 0
    current_position = start_position
    for i in puzzle:
        current_position += i
        if current_position == mod:
            continue
        pwd += abs(current_position // mod)

        current_position = current_position % mod

    return pwd


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
