from typing import Tuple
from elf_machine import ElfMachine
import string


def find_start(rows: list[str]):
    for index, row in enumerate(rows):
        col = row.find("S")
        if col >= 0:
            return (index, col)


def find_lowest_elevations(rows: list[str]):
    points = set()
    for r_index, row in enumerate(rows):
        for c_index, col in enumerate(row):
            if col in ["S", "a"]:
                points.add((r_index, c_index))

    return list(points)


def find_end(rows: list[str]):
    for index, row in enumerate(rows):
        col = row.find("E")
        if col >= 0:
            return (index, col)


#  increasing as in a -> z
def determine_possible_moves_inc(rows: list[str], cur: Tuple[int, int]):
    value = rows[cur[0]][cur[1]]
    if value == "S":
        value = 0
    elif value == "E":
        value = 25

    possible_next_steps = []

    # check up
    if cur[0] > 0:
        up = rows[cur[0] - 1][cur[1]]
        if up <= value + 1:
            possible_next_steps.append((cur[0] - 1, cur[1]))

    # check down
    if cur[0] < len(rows) - 1:
        down = rows[cur[0] + 1][cur[1]]
        if down <= value + 1:
            possible_next_steps.append((cur[0] + 1, cur[1]))

    # check left
    if cur[1] > 0:
        left = rows[cur[0]][cur[1] - 1]
        if left <= value + 1:
            possible_next_steps.append((cur[0], cur[1] - 1))

    # check right
    if cur[1] < len(rows[0]) - 1:
        right = rows[cur[0]][cur[1] + 1]
        if right <= value + 1:
            possible_next_steps.append((cur[0], cur[1] + 1))

    return possible_next_steps


def determine_possible_moves_desc(rows: list[str], cur: Tuple[int, int]):
    value = rows[cur[0]][cur[1]]
    if value == "S":
        value = 0
    elif value == "E":
        value = 25

    possible_next_steps = []

    # check up
    if cur[0] > 0:
        up = rows[cur[0] - 1][cur[1]]
        if up == value - 1 or up == value:
            possible_next_steps.append((cur[0] - 1, cur[1]))

    # check down
    if cur[0] < len(rows) - 1:
        down = rows[cur[0] + 1][cur[1]]
        if down == value - 1 or down == value:
            possible_next_steps.append((cur[0] + 1, cur[1]))

    # check left
    if cur[1] > 0:
        left = rows[cur[0]][cur[1] - 1]
        if left == value - 1 or left == value:
            possible_next_steps.append((cur[0], cur[1] - 1))

    # check right
    if cur[1] < len(rows[0]) - 1:
        right = rows[cur[0]][cur[1] + 1]
        if right == value - 1 or right == value:
            possible_next_steps.append((cur[0], cur[1] + 1))

    return possible_next_steps


class Day12(ElfMachine):
    def solve_first_puzzle(self, input_data: str) -> int:
        rows = input_data.split("\n")

        start = find_start(rows)
        end = find_end(rows)

        normalized_rows = []
        height_map = {"S": 0, "E": 25}
        for row in rows:
            normalized = [
                string.ascii_letters.index(item)
                if item not in ["S", "E"]
                else height_map[item]
                for item in row
            ]
            normalized_rows.append(normalized)

        queue = [[start]]
        visited = []

        while queue:
            path = queue.pop(0)
            cur = path[-1]

            if cur not in visited:
                next_steps = determine_possible_moves_inc(normalized_rows, cur)

                for step in next_steps:
                    new_path = list(path)
                    new_path.append(step)
                    queue.append(new_path)

                    if step == end:
                        return len(new_path) - 1

                visited.append(cur)

    def solve_second_puzzle(self, input_data: str) -> int:
        rows = input_data.split("\n")

        starting_points = find_lowest_elevations(rows)
        end = find_end(rows)

        normalized_rows = []
        height_map = {"S": 0, "E": 25}
        for row in rows:
            normalized = [
                string.ascii_letters.index(item)
                if item not in ["S", "E"]
                else height_map[item]
                for item in row
            ]
            normalized_rows.append(normalized)

        path_lengths = []
        for index, start in enumerate(starting_points):
            queue = [[start]]
            visited = []

            while queue:
                path = queue.pop(0)
                cur = path[-1]

                if cur not in visited:
                    next_steps = determine_possible_moves_inc(normalized_rows, cur)

                    for step in next_steps:
                        new_path = list(path)
                        new_path.append(step)
                        queue.append(new_path)

                        if step == end:
                            path_lengths.append(len(new_path) - 1)
                            break

                    visited.append(cur)

        return sorted(path_lengths)[0]
