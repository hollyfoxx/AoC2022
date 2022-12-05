import string

from elf_machine import ElfMachine


class Day5(ElfMachine):
    def solve_first_puzzle(self, input_data: str) -> int:
        crate_section, instruction_section = input_data.split("\n\n")

        # Parse starting crates
        crate_map = []
        for layer in crate_section.split("\n")[::-1]:

            if layer.startswith(" 1"):
                continue

            split_layer = layer.split("    ")
            split_layer = list(map(lambda x: x.split(" "), split_layer))
            crates = []
            for sublist in split_layer:
                crates.extend(sublist)

            for index, crate in enumerate(crates):
                if crate == "":
                    continue

                if len(crate_map) < len(crates):
                    crate_map.append([crate])

                else:
                    crate_map[index].append(crate)

        # Parse instructions
        parsed_instructions = []
        for instruction in instruction_section.split("\n"):
            parsed_instruction = instruction.split("move ")[1]
            move_count, parsed_instruction = parsed_instruction.split(" from ")
            from_stack, to_stack = parsed_instruction.split(" to ")

            # perform moves
            for count in range(0, int(move_count)):
                crate_map[int(to_stack) - 1].append(
                    crate_map[int(from_stack) - 1].pop()
                )

        top_crates = ""
        for stack in crate_map:
            top_crates = f"{top_crates}{stack.pop()[1:2]}"

        return top_crates

    def solve_second_puzzle(self, input_data: str) -> str:
        return False
