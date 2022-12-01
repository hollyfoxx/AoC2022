from abc import ABC, abstractmethod
from typing import Union


class ElfMachine(ABC):
    def read_input(self, path: str):
        with open(path) as f:
            return f.read()

    @abstractmethod
    def solve_first_problem(self, input_data: Union[str, list[str]]) -> Union[int, str]:
        pass

    @abstractmethod
    def solve_second_problem(self, input_data: str) -> Union[int, str]:
        pass
