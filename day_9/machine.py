from typing import Tuple
from elf_machine import ElfMachine


def is_adjacent(tail: list[int], head: list[int, int]):
    # on top of each other
    if tail[0] == head[0] and tail[1] == head[1]:
        return True

    # same col (x), different row (y)
    if tail[0] == head[0] and tail[1] == head[1] - 1:
        return True

    if tail[0] == head[0] and tail[1] == head[1] + 1:
        return True

    # same row (y), different col (x)
    if tail[0] == head[0] + 1 and tail[1] == head[1]:
        return True

    if tail[0] == head[0] - 1 and tail[1] == head[1]:
        return True

    # lower right diagonal
    if tail[0] == head[0] + 1 and tail[1] == head[1] + 1:
        return True

    # upper left diagonal
    if tail[0] == head[0] - 1 and tail[1] == head[1] - 1:
        return True

    # upper right diagonal
    if tail[0] == head[0] + 1 and tail[1] == head[1] - 1:
        return True

    # lower left diagonal
    if tail[0] == head[0] - 1 and tail[1] == head[1] + 1:
        return True

    return False


def move_tail(tail: list[int], head: list[int]):
    # same col (x), different row (y)
    if tail[0] == head[0] and tail[1] > head[1]:
        return (tail[0], tail[1] - 1)

    if tail[0] == head[0] and tail[1] < head[1]:
        return (tail[0], tail[1] + 1)

    # same row (y), different col (x)
    if tail[0] > head[0] and tail[1] == head[1]:
        return (tail[0] - 1, tail[1])

    if tail[0] < head[0] and tail[1] == head[1]:
        return (tail[0] + 1, tail[1])

    # lower right diagonal
    if tail[0] < head[0] and tail[1] < head[1]:
        return (tail[0] + 1, tail[1] + 1)

    # upper left diagonal
    if tail[0] > head[0] and tail[1] > head[1]:
        return (tail[0] - 1, tail[1] - 1)

    # upper right diagonal
    if tail[0] < head[0] and tail[1] > head[1]:
        return (tail[0] + 1, tail[1] - 1)

    # lower left diagonal
    if tail[0] > head[0] and tail[1] < head[1]:
        return (tail[0] - 1, tail[1] + 1)


def print_map(size, tail, head):
    rope_map = []
    for _ in range(0, size[1]):
        rope_map.append(list("." * size[0]))

    rope_map[tail[1] + 5][tail[0] + 5] = "T"
    rope_map[head[1] + 5][head[0] + 5] = "H"

    for row in rope_map:
        print("".join(row))

    print("\n")


class Day9(ElfMachine):
    def solve_first_puzzle(self, input_data: str) -> int:
        movements = input_data.split("\n")

        head = [0, 0]
        tail = [0, 0]

        visited = set()

        for move in movements:
            direction, count = move.split(" ")
            for _ in range(0, int(count)):
                visited.add(f"{tail[0]}_{tail[1]}")

                if direction == "R":
                    head[0] += 1
                elif direction == "U":
                    head[1] -= 1
                elif direction == "L":
                    head[0] -= 1
                elif direction == "D":
                    head[1] += 1

                if not is_adjacent(tail, head):
                    tail = move_tail(tail, head)

        visited.add(f"{tail[0]}_{tail[1]}")
        return len(visited)

    def solve_second_puzzle(self, input_data: str) -> str:
        movements = input_data.split("\n")

        head = [0, 0]
        one = [0, 0]
        two = [0, 0]
        three = [0, 0]
        four = [0, 0]
        five = [0, 0]
        six = [0, 0]
        seven = [0, 0]
        eight = [0, 0]
        nine = [0, 0]
        tail = [0, 0]

        visited = set()

        for move in movements:
            direction, count = move.split(" ")
            for _ in range(0, int(count)):
                visited.add(f"{tail[0]}_{tail[1]}")

                if direction == "R":
                    head[0] += 1
                elif direction == "U":
                    head[1] -= 1
                elif direction == "L":
                    head[0] -= 1
                elif direction == "D":
                    head[1] += 1

                if not is_adjacent(nine, head):
                    nine = move_tail(nine, head)

                if not is_adjacent(eight, nine):
                    eight = move_tail(eight, nine)

                if not is_adjacent(seven, eight):
                    seven = move_tail(seven, eight)

                if not is_adjacent(six, seven):
                    six = move_tail(six, seven)

                if not is_adjacent(five, six):
                    five = move_tail(five, six)

                if not is_adjacent(four, five):
                    four = move_tail(four, five)

                if not is_adjacent(three, four):
                    three = move_tail(three, four)

                if not is_adjacent(two, three):
                    two = move_tail(two, three)

                if not is_adjacent(tail, two):
                    tail = move_tail(tail, two)

        visited.add(f"{tail[0]}_{tail[1]}")
        return len(visited)
