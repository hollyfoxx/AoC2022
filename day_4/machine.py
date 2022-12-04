import string

from elf_machine import ElfMachine


class Day4(ElfMachine):
    def solve_first_puzzle(self, input_data: str) -> int:
        pairs = input_data.split("\n")

        subset_count = 0 
        for pair in pairs:
            elf_a, elf_b = pair.split(",") 
            elf_a_start, elf_a_end = elf_a.split("-")
            elf_a_range = set(range(int(elf_a_start), int(elf_a_end) + 1))

            elf_b_start, elf_b_end = elf_b.split("-")
            elf_b_range = set(range(int(elf_b_start), int(elf_b_end) + 1))

            if elf_a_range.issubset(elf_b_range) or elf_b_range.issubset(elf_a_range):
                subset_count += 1

        return subset_count

    def solve_second_puzzle(self, input_data: str) -> str:
        pairs = input_data.split("\n")

        overlap_count = 0 
        for pair in pairs:
            elf_a, elf_b = pair.split(",") 
            elf_a_start, elf_a_end = elf_a.split("-")
            elf_a_range = set(range(int(elf_a_start), int(elf_a_end) + 1))

            elf_b_start, elf_b_end = elf_b.split("-")
            elf_b_range = set(range(int(elf_b_start), int(elf_b_end) + 1))

            if elf_a_range.intersection(elf_b_range):
                overlap_count += 1

        return overlap_count