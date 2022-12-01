from elf_machine import ElfMachine


class Day0(ElfMachine):
    def execute(self, input_data: str) -> str:
        return f"{input_data} world"
