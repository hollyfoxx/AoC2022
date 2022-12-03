import string

from elf_machine import ElfMachine


class Day3(ElfMachine):
    def solve_first_puzzle(self, input_data: str) -> int:
        rucksacks = input_data.split("\n")
        priority_sum = 0
        for rucksack in rucksacks:
            compartment_size = int(len(rucksack) / 2)
            compartment_one = set(rucksack[:compartment_size])
            compartment_two = set(rucksack[compartment_size:])

            item = compartment_one.intersection(compartment_two).pop()
            priority_sum += string.ascii_letters.index(item) + 1

        return priority_sum

    def solve_second_puzzle(self, input_data: str) -> str:
        return False
