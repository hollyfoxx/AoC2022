import json
from elf_machine import ElfMachine


class Day13(ElfMachine):
    def solve_first_puzzle(self, input_data: str) -> int:
        pairs = input_data.split("\n\n")

        correct_pair_indices = []
        for index, pair in enumerate(pairs):
            left, right = pair.split("\n")
            left = json.loads(left)
            right = json.loads(right)

    def solve_second_puzzle(self, input_data: str) -> int:
        return False
