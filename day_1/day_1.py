from elf_machine import ElfMachine


class Day1(ElfMachine):
    def solve_first_puzzle(self, input_data: list[str]) -> int:
        calories = input_data.split("\n")

        most_calories = 0
        current_elf_count = 0
        for item in calories:
            if item == "":
                if current_elf_count > most_calories:
                    most_calories = current_elf_count
                current_elf_count = 0
                continue

            current_elf_count += int(item)

        return most_calories

    def solve_second_puzzle(self, input_data: str) -> str:
        raise NotImplementedError
